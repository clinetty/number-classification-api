# Number Classification API

An API that takes a number and returns interesting mathematical properties about it, along with a fun fact.

## Functionality
- Accepts GET requests with a number parameter.
- Returns JSON in the specified format.
- Accepts all valid integers as the only possible inputs
- Provides appropriate HTTP status codes.
- Fun fact retrieval

## Usage
### Endpoint
`GET** <your-url>/api/classify-number?number=371`

### Example Response
Required JSON Response Format (200 OK)

```
{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,  // sum of its digits
    "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}

```

Required JSON Response Format (400 Bad Request)

```
{
    "number": "alphabet",
    "error": true
}

```

## Installation & running instructions
To get the Number Classification API up and running on your local machine, follow the steps below:

### Prerequisites
- Python 3.7+ is required.
- Pip should be installed.

#### 1. Clone the Repository

```
git clone https://github.com/your-username/number-classification-api.git
cd number-classification-api

```

#### 2. Create a Virtual Environment

```
python -m venv venv

```

Activate the virtual environment:

```
source venv/bin/activate # On Windows: venv\Scripts\activate

```

#### 3. Install Dependencies

```

pip install -r requirements.txt

```

#### 4. Run the API Locally

```

uvicorn main:app --reload

```

#### 5. Access the API

```

http://127.0.0.1:8000/api/classify-number?number=371

```

## Deployment link
