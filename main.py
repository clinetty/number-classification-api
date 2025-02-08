from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import requests

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n: int) -> bool:
    return sum(i for i in range(1, n) if n % i == 0) == n

def is_armstrong(n: int) -> bool:
    digits = [int(d) for d in str(n)]
    return sum(d ** len(digits) for d in digits) == n

def get_fun_fact(n: int) -> str:
    if is_armstrong(n):
        digits = [int(d) for d in str(n)]
        equation = " + ".join([f"{d}^{len(digits)}" for d in digits])
        return f"{n} is an Armstrong number because {equation} = {n}"
    else:
        response = requests.get(f"http://numbersapi.com/{n}/math?json")
        return response.json().get("text", "No fun fact available.")

@app.get("/api/classify-number")
def classify_number(number: str = Query(..., description="The number to classify")):
    if not number.lstrip("-").isdigit():
        return JSONResponse(
            status_code=400,
            content={"number": number, "error": True},
        )
    
    number = int(number)
    properties = ["odd" if number % 2 else "even"]
    if is_armstrong(number):
        properties.insert(0, "armstrong")

    # Formatted digit_sum with the comment at the end, no comma after the comment
    digit_sum = f"{sum(int(digit) for digit in str(abs(number)))} // sum of its digits"

    response = {
        "number": number,
        "is_prime": is_prime(number),
        "is_perfect": is_perfect(number),
        "properties": properties,
        "digit_sum": digit_sum,  # sum of digits with the comment
        "fun_fact": get_fun_fact(number),
    }
    return response