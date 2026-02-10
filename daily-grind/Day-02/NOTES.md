# Day 2 - Routing & API Design



### What is Routing?
- routing is the process of deciding:

    >when a request comes to this URL with this HTTP method, which piece of code should handle it?

    - for example: `GET /users`
    - router decision: "call the function that returns users"
- to paint this clearly, routing basically is like a reception desk:
    - the URL is the user's request, and the HTTP method is what they want to do.
    - the router sends them to the correct office

### What is API design?

- in routing context, it is where does this request go?
- in API design, how should clients interact with this system?

- API design cares about:
    - naming, consistency, predictability, long-term maintainance.


## 1. API Versioning (/api/v1)

- why does versioning exists?? let's take for example we have a mobile app that uses our API. if we were to suddenly change/update how `/users` works, the app will crash for thousands of users.
- versioning helps us prevent this. rather than changing existing behaviour, we create a new version and keep old clients app working on the old version.

**What does /api/v1 actually means?**

- /api tell everyone that this is not a website but instead a machine-readable interface.
- /v1 is a contract version:
    - v1 = first public promise
    - Note: this shouldn't be broken silently

- API versioning protects clients from breaking changes by isolating behaviour into versions
- URL typically follow `/api/v{number}/resource`


## 2. RESTful Route Design

- REST is way of organizing URLs so that they represent things (resources).
    - Note: not actions
- e.g., users, products, others etc

- REST APIs use nouns (resources) in URLs and HTTP methods to describe actions.

- good example of a resource-based API

```code
GET   /users
POST  /users
GET  /users/42
DELETE  /users/42
```

```python
from fastapi import APIRouter

router = APIRouter(prefix="/items", tags=["items"])

```

- `prefix="/items"` all item routes start with `/items`
- `tags=["items"] groups endpoints in /docs
    - this is purely for documentation

### Pagination

- why do we use pagination??
    - suppose we have a database with 10K users. if for some reason we decide to return all of them, we will overwhelm our DB resulting in slow response, high memory usage, and client freezes.

- pagination is basically the concept of giving a slice of data not everything. 
- it limits result size using query params like `page` and `limit` to improve performance and usability.
- for example:

```code
/users?page=1&limit=10
```
- this means: we return only page 1 and limit users to 10 per page. 
- query params modify how data is returned


### filtering [narrowing results]

- filtering allows clients to narrow results using optional query params.
- in real world use cases, clients rarely want everything. 
- examples:
    - only admin users
    - only completed orders
    - only active products

```code
/users?role=admin
```

### sorting [ordering data]

- sorting controls the order of results and should be limited to approved fields.
- why sorting is needed??
    - different clients want newest first, olders first, alphabetical order

```code
/users?sort_by=created_at&order=desc
```
- sort users, by creation time & newest first.
- Note: never allow arbitrary fields or unvalidated input


## 3. Route Grouping

- a router is container for related routes (usually one route per resource) for example `users_router`, `items_router`
- routers group related endpoints, improving maintainability and scalability


## 4. OpenAPI Documentation

- openAPI is a machine-readable API description used to generate docs, clients, and tests
- it describes endpoints, params, and responses in a standardized format.
- FastAPI can be used to automatically generate it if we add metadata. 


## 5. Error Handling Patterns

- API should return consistent, meaningful error responses using appropriate HTTP status codes



- pagination controls how much you get.
- filtering controls which ones you get.