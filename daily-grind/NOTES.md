# Day 1 - HTTP Basics

### Objectives

- [ ] running FastAPI server
- [ ] few deliberately simple endpoints
- [ ] ability to inspect incoming HTTP requests
- [ ] logging middleware (understanding request flow)
- [ ] README.md scaffold


## Feature 1: Core Endpoints

**1.1 Feature Overview**

- implement three endpoints: `GET /health` [service health check], `POST /echo` [inspect request bodies], and `GET /status/{code}` [understand HTTP status codes].

    - health check -> load balances, Kubernetes, uptime monitoring
    - echo endpoints -> debugging, contract testing, learning
    - status endpoints -> testing client-side error handling



1. `GET /health`

- when is it used?? To check if the server is alive.
- we send a HTTP `GET` request and get a JSON response with a status code. 
- Note: always important to return a predictable JSON shape and status `200 OK`

- visiting `/health should return
```json
{ "status": "ok" }
```

> HTTP status code is `200`

**Common Mistakes**

- returning a plain text instead of JSON
- forgetting to specify response format
- using the wrong HTTP method.


2. `POST /echo`

- what is the purpose?? To see what exactly the client sends.

- send a HTTP `POST` together with a request body, and JSON parsing.
    - parsing JSON referes to the process of taking JSON-formatted data and converting it into a data structure that a program can work with. 

- should receive the same JSON back:
```json
{ "message": "hello" }
```

**Commnon Mistakes**
- using `GET` instead of `POST`
- forgetting to parse JSON (JavaScript Object Notation)
- assuming a schema too early.

3. `GET /status/{code}`

- what is the purpose?? To demonstrate and test how clients  handle different HTTP response status codes. 
    - this is useful for client-side error handling logic, observing how browsers, SDKs, and API consumers react to non-200 responses. 

- conceptually:
    -  path parameters [`{code}` is a dynamic path parameter extracted from the URL]
    -  dynamic HTTP status codes [the server responds with the status code provided in the path, rather than always returning `200` OK]
    - HTTP semantics [these reinforces the meaning and usage of status codes]

- QUE: why this matters?
    - in real systems, clients must not assume success.
    - proper handling depends on status codes, not just response bodies.
    - this endpoint isolates status-code behavior without business logic noise.


## Feature 2: Inspecting the Request

**2.1 Feature Overview**

- what headers did the client send?
- what query parameters were provided
- are cookies present?

1. Headers

- headers carry metadata:
    - authentication
    - content type
    - user agent
    - tracing IDs

- QUE: how do verify this??
    - print or return headers
    - confirming can see: `User-Agent`, `Accept`, `Content-Type`. 

2. Query Parameters

- query params modify requests without changing endpoints. 
- Example:

```bash
/echo?debug=true&limit=10
```

- QUE: how do we verify this?
    - access values individually
    - confirm types (everything starts as a string)

3. Cookies

- cookies are client-stored state send on every request

- Que: verification??
    - send a cookie from your client
    - confirm the server can read it


## Feature 3: Logging Middleware

**3.1 Feature Overview

- middleware runs:
    - before the request reaches the endpoint
    - after the response leaves the endpoint

- Que: what is it used for??
    - logging, authentication, metrics, tracing

1. Basic Logging Middleware

- in backend services, requests don't execute in isolation. without centralised logging, we have no visibility into:
    - which endpoints are being called
    - how frequently they are hit
    - whether requests are succeeding or failing
    - how long each request takes to process. 

- sometimes logging inside individual endpoints doesn't scale and leads to duplicated, inconsistent logs. thus, we need a singlw interception point that observes every request.

- middleware lifecycle:
    1. request enters the application
    2. middleware executes before the endpoint
    3. endpoint handler runs
    4. middleware executes after the response is generated
    5. response is returned to the client. 

- request/response timing:
    - middleware can record a start time before forwarding the request
    - after the response returns, middleware calculates total execution time
    - this allows performance monitoring without modifying endpoint logic

- middleware is the architectural layer for cross-cutting concerns such as:
    - logging, authentication, rate limiting, metrics, and tracing. 

- logging fields:
    1. HTTP method 
        - indicates the type of operation (`GET`, `POST`, `PUT`, `DELETE`)
    2. Path
        - identifies which response or endpoint was accessed
    3. Status code
        - shows whether the request succeeded, failed due to client error, or failed due to server error
    4. Execution time
        - measures total time spent procesing the request (in milliseconds). 

Note: these fields are sufficient to debug 80-90% of API issues, keep logs readable and low-noise. 
- every incoming request should produce a log entry similar to:
    ```code
    GET /health → 200 (3.2ms)
    ```
    
    - confirms the request passed through middleware. endpoint executed successfully. the response time was measure and the response was returned correctly.

- some of the common failures:
    1. blocking the request
        - forgetting to call the next handler in the middleware chain. and the request never reaches endpoint, causing timeouts.
    2. forgetting to return the response
        - middleware calls the next handler but doesn't return the response object. client receives no response or FastAPI raises an error.
    3. logging inside endpoints instead of middleware
        - leads to duplicated logging logic across endpoints. misses failed requests that never reach the handler and violates separation of concerns.
    4. measuring time incorrectly
        - starting the timer after the request is forwarded. stopping the time before the response is returned which results in misleading performance data.