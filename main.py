from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import math

app = FastAPI()

class NumberRequest(BaseModel):
    number: float 

@app.get("/api/classify-number")
async def classify_number(request: NumberRequest):
    number = request.number

    if not isinstance(number, (int, float)):
        raise HTTPException(status_code=400, detail="Number must be numeric.")

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True

    def is_perfect(num):
        divisors = [i for i in range(1, num) if num % i == 0]
        return sum(divisors) == num

    def digit_sum(num):
        return sum(int(digit) for digit in str(abs(num)))

    def get_fun_fact(num):
        digits = str(abs(num))
        power = len(digits)
        sum_of_powers = sum(int(digit) ** power for digit in digits)
        if sum_of_powers == abs(num):
            return f"{num} is an Armstrong number because " + " + ".join([f"{d}^{power}" for d in digits]) + f" = {num}"
        return f"{num} is a special number."

    return {
        "number": number,
        "is_prime": is_prime(number),
        "is_perfect": is_perfect(number),
        "properties": ["armstrong" if get_fun_fact(number).startswith(f"{number} is an Armstrong") else "odd" if number % 2 != 0 else "even"],
        "digit_sum": digit_sum(number),
        "fun_fact": get_fun_fact(number)
    }
