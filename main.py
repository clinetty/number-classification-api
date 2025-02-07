from fastapi import FastAPI, Query, HTTPException
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
    digits = [int(d) for d in str(abs(n))]  # Handle negatives correctly
    return sum(d ** len(digits) for d in digits) == abs(n)

def get_fun_fact(n: float) -> str:
    if is_armstrong(int(n)):  # Convert to int before checking Armstrong property
        digits = [int(d) for d in str(abs(int(n)))]  
        equation = " + ".join([f"{d}^{len(digits)}" for d in digits])
        return f"{int(n)} is an Armstrong number because {equation} = {int(n)}"
    else:
        response = requests.get(f"http://numbersapi.com/{int(n)}/math?json")
        return response.json().get("text", "No fun fact available.")

@app.get("/api/classify-number")
def classify_number(number: str = Query(..., description="The number to classify")):
    try:
        # Allow integer and floating-point numbers
        if "." in number:
            number = float(number)
        else:
            number = int(number)
    except ValueError:
        raise HTTPException(status_code=400, detail="Number must be numeric.")

    properties = ["odd" if isinstance(number, int) and number % 2 else "even"]
    if isinstance(number, int) and is_armstrong(number):
        properties.insert(0, "armstrong")

    response = {
        "number": number,
        "is_prime": is_prime(int(number)),  # Ensure only integers are passed
        "is_perfect": is_perfect(int(number)),  # Ensure only integers are passed
        "properties": properties,
        "digit_sum": sum(int(digit) for digit in str(abs(int(number)))),  # Ensure integer digit sum
        "fun_fact": get_fun_fact(number),
    }
    
    return JSONResponse(status_code=200, content=response)
