from fastapi import FastAPI, HTTPException
from typing import Union

app = FastAPI()

def check_prime(number: Union[int, float]) -> bool:
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def check_perfect(number: Union[int, float]) -> bool:
    if number <= 0:
        return False
    divisors_sum = sum(i for i in range(1, int(number)) if number % i == 0)
    return divisors_sum == number

def check_properties(number: Union[int, float]) -> list:
    num_str = str(abs(int(number)))
    power = len(num_str)
    digit_sum = sum(int(digit)**power for digit in num_str)
    properties = []
    if digit_sum == abs(int(number)):
        properties.append("armstrong")
    if number % 2 == 0:
        properties.append("even")
    else:
        properties.append("odd")
    return properties

def get_fun_fact(number: Union[int, float]) -> str:
    if number == 371:
        return "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
    return f"{number} is a special number."

def classify_number(number: Union[int, float]):
    is_prime = check_prime(number)
    is_perfect = check_perfect(number)
    properties = check_properties(number)
    digit_sum = sum(int(digit) for digit in str(abs(int(number))))
    fun_fact = get_fun_fact(number)
    
    return {
        "number": number,
        "is_prime": is_prime,
        "is_perfect": is_perfect,
        "properties": properties,
        "digit_sum": digit_sum,
        "fun_fact": fun_fact
    }

@app.get("/api/classify-number")
async def get_number_classification(number: str):
    try:
        num = float(number)
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid number format.")
    
    return classify_number(num)
