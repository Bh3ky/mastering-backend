from fastapi import FastAPI, Request, Response
from fastapi.responses import JSONResponse
import time
import logging

# set up the application object
app = FastAPI()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# middleware
@app.middleware("http")
async def log_requests(request: Request, call_next):
    start_time = time.time()

    response = await call_next(request)

    duration_ms = (time.time() - start_time) * 1000

    logger.info(
        "%s %s -> %s (%.2fms)",
        request.method,
        request.url.path,
        response.status_code,
        duration_ms,
    )

    return response

# GET /health
@app.get("/health")
async def health(request: Request):
    # inspect request metadata
    headers = dict(request.headers)
    query_params = dict(request.query_params)
    cookies = request.cookies

    logger.debug("Headers: %s", headers)
    logger.debug("Query params: %s", query_params)
    logger.debug("Cookies: %s", cookies)

    return {"status": "ok"}


# POST /echo
@app.post("/echo")
async def ech(payload: dict):
    return payload


# GET /status/{code}
@app.get("/status/{code}")
async def return_status(code: int):
    return Response(status_code=code)