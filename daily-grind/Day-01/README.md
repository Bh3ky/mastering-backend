## Day 1 - HTTP Basics with FastAPI

This mini project demonstrate core HTTP concepts using FastAPI.

### Features
- health check endpoint
- echo endpoint
- dynamic status code responses
- request inspection (headers, query params, cookies)
- basic logging middleware

### Running Locally

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Endpoints
- `GET /health` → basic health check
- `POST /echo` → echoes JSON request body
- `GET /status/{code}` → returns a chosen HTTP status code
- `GET /inspect` → returns headers, query params, and cookies