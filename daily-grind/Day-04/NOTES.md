# Validation & Middleware

**Question: what is validation??**
- validation is the process of checking whether incoming data:
    - exists
    - has the correct type
    - follows business rules
    - is safe to process

- e.g., a user registration API may require:
    - valid email, password of length ≥ 8, and age ≥ 8.

- without validation, invalid data can enter our system corrupt the database or even worse increase the chances of a crash. security vulnerabilities appear. 

**Client-Side vs Server-Side Validation**

- client-side validation runs in the browser, mobile app, and frontend.

```js
if (password.length < 8)
```

Purpose: 
- improve UX and instant feedback.

Problem:
- cannot be trusted

attackers can bypass frontend validation completely.

- server-side validation runs on backend server
    - NB: this is the real security boundary

- the server must assume:

> "every client request may be malicious or malformed."

- thus, the need to ALWAYS validate on the server.



## Pydantic Schemas

**Question: what is Pydantic??**
- Pydantic is a Python library which is used for data validation, parsing, serialization, and type enforcement.

FastAPI heavily depends on it.

**Question: why Pydantic exists??**

- without schemas:

```python
data = request.json()

email = data["email"]
age = int(data["age"])
```

- here, from the code snippet we have a couple problems:
    - missing keys, wrong types
    - repetitive checks, messy code

- Pydantic centralises all validation rules

### Core Concept: Schema

- a schema defines:
    - expected fields, types, constraints, and validation rules. for example:

```python
from pydantic import BaseModel, EmailStr, Field

class UserCreate(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8)
    age: int = Field(gt=0)
```

- FastAPI receives JSON and converts it into Python objects, validates fields, and return errors automatically if invalid.
- NB: this is extremely important architecturally. 

The endpoint only executes if validation succeeds.

**Example: Request Flow**

- client sends:

```JSON
{
  "email": "bad-email",
  "password": "123",
  "age": -1
}
```

- FastAPI/Pydantic rejects requests BEFORE the client's route logic runs.

Response:

```json
{
  "detail": [
    {
      "loc": ["body", "email"],
      "msg": "value is not a valid email"
    }
  ]
}
```

### Important Pydantic Concepts

**BaseModel**
- all schemas inherit from `BaseModel`

```python
class Product(BaseModel):
    name: str
```

- this enables validation, serialization, and parsing. 


**Type Enforcement**

```python
price: float
```

- Pydantic checks type correctness automatically. 


**Field Constraints**

```python
from pydantic import Field

username: str = Field(min_length=3, max_length=20)
```

- common constraints:
    - `min_length`
    - `max_length`
    - `gt`
    - `lt`
    - `ge`
    - `le`
    `regex`


**Specialised Types**

```python
EmailStr
AnyUrl
UUID4
datetime
```

- these reduce manual validation code.


**Nested Schemas**

```python
class Address(BaseModel):
    city: str
    country: str

class User(BaseModel):
    name: str
    address: Address 
```

- critical for real APIs.


**Optional Fields**

```python
from typing import Optional

bio: Optional[str] = None
```

- production APIs usually seperate schemas by purpose. e.g.,:

```text
schemas/
├── user.py
```

- inside:

```python
UserCreate
UserLogin
UserResponse
UserUpdate
```

**Question: why is it important to seperate schemas??**
- because different operations require different fields. 

- Example:
    - UserCreate -> password required
    - UserResponse -> password hidden
    - UserUpdate -> optional fields

- this prevents leaking sensitive data, invalid API design, and coupling. 


## Input Sanitization

**Validation vs Sanitization**

| Validation | Sanitization |
| -- | -- |
| checks if input is acceptable | cleans/modifies input |
| rejects bad data | transforms data |
| "is this valid?" | "make this safe/consistent" |

Examples of Sanitization

1. trim whitespace

```python
name = name.strip()
```

2. normalize email

```python
email = email.lower()
```

3. remove dangerous HTML

- need to prevent _XSS attacks and script injection_.

- E.g., dangerous input:

```HTML
<script>alert("hacked")</script>
```

- validation alone does NOT stop:
    - XSS 
    - SQL injection
    - command injection

- sanization + parameterized queries + escaping are also required.


**Pydantic Validators**

```python
from pydantic import BaseModel, field_validator

class UserCreate(BaseModel):
    email: str

    @field_validator("email")
    @classmethod
    def normalize_email(cls, value):
        return value.strip().lower()
```

- this is both validation + sanitization. 


## Middleware

**Question: what is Middleware??**
- Middleware is code that executes:
    - BEFORE request reaches route,
    - AFTER route returns response


**Middleware Execution Flow**

```text
Client Request
      ↓
Middleware
      ↓
Route Handler
      ↓
Middleware
      ↓
Client Response
```

**Question: why does Middleware exists??**

- Middleware centralizes cross-cutting concerns.
- without middleware:
    - repeated code everywhere
    - inconsistent behaviour
    - poor maintainability


### Common Middleware Responsibilities

| Responsibility | Purpose |
| -- | -- |
| logging | track requests |
| authentication | verify users |
| CORS | cross-origin control |
| timing | performance metrics |
| request IDs | traceability |
| rate limiting | abuse prevention |
| compression | faster responses |
| error handling | consistent responses |


## Request ID Middleware

**Problem**

in production:
- thousands of requests occur simultaneously

how do you trace:
- logs, errors, database operations for ONE specific request??

- have to attach a unique request ID


**Request ID Concept**

```text
X-Request-ID: a1b2c3d4
```

- every log line includes that ID and this make debugging possible.

Example: Request ID Middleware

```python
import uuid
import time

from fastapi import FastAPI, Request

app = FastAPI()

@app.middleware("http")
async def add_request_id(request: Request, call_next):

    request_id = str(uuid.uuid4())

    request.state.request_id = request_id

    response = await call_next(request)

    response.headers["X-Request-ID"] = request_id

    return response
```

**what's going on here???**
- `request.state` is a temporary request-scoped storage. it is useful for request IDs, authenticated user, and timing metadata.
- `call_next(request)` passes request to the next middleware, then eventually a route handler. 
    - middleware wraps around request lifecycle.


## Execution Timing Middleware

- purpose?? measures request duration
    - critical for:
        - performance monitoring
        - identifying slow endpoints
        - observability

```python
import time

@app.middleware("htpp")
async def add_process_time(request: Request, call_next):

    start_time = time.perf_counter()

    response = await call_next(request)

    duration = time.perf_counter() - start_time

    response.headers["X-Process-Time"] = str(duration)

    return response
```

**why `perf_counter()` ??**
- better precision for timing measurement.


## Centralised Error Responses

- without centralization routes return different error formats. thus we have to create consistent API responses.

Example:

```JSON
{
  "success": false,
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Invalid input"
  }
}
```

### FastAPI Exception Handling

```python
from fastapi import Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(
    request: Request,
    exc: RequestValidationError
):

    return JSONResponse(
        status_code=422,
        content={
            "success": False,
            "error": {
                "code": "VALIDATION_ERROR",
                "details": exc.errors()
            }
        }
    )
```

- centralised errors are critical for:
    - frontend consistency
    - monitoring systems
    - API consumers
    - debugging
    - observability

- a mature backend usually validates at multiple layers

```text
Client Validation
        ↓
API Schema Validation
        ↓
Business Rule Validation
        ↓
Database Constraints
```

## Middleware Pipeline Diagram

```text
                Incoming Request
                        ↓
        ┌──────────────────────────┐
        │ Request ID Middleware    │
        │ Generate UUID            │
        └──────────────────────────┘
                        ↓
        ┌──────────────────────────┐
        │ Timing Middleware        │
        │ Start performance timer  │
        └──────────────────────────┘
                        ↓
        ┌──────────────────────────┐
        │ Validation Layer         │
        │ Pydantic schema checks   │
        └──────────────────────────┘
                        ↓
        ┌──────────────────────────┐
        │ Route Handler            │
        │ Business logic           │
        └──────────────────────────┘
                        ↓
        ┌──────────────────────────┐
        │ Error Handler            │
        │ Standardize errors       │
        └──────────────────────────┘
                        ↓
        ┌──────────────────────────┐
        │ Timing Middleware        │
        │ Attach duration header   │
        └──────────────────────────┘
                        ↓
        ┌──────────────────────────┐
        │ Request ID Middleware    │
        │ Attach request ID header │
        └──────────────────────────┘
                        ↓
                 HTTP Response
```

