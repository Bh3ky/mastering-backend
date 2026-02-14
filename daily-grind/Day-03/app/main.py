import hashlib
import time
import json
from fastapi import FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

app = FastAPI()


# CORS config

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# rate limit config

RATE_LIMIT = 5
WINDOW_SECONDS = 60
rate_limit_store = {}


# rate limit middleware

@app.middleware("http")
async def rate_limit_middleware(request: Request, call_next):
    client_ip = request.client.host
    current_time = time.time()
    
    if client_ip not in rate_limit_store:
        rate_limit_store[client_ip] = {
            "count": 1,
            "window_start": current_time
        }
    else:
        window = rate_limit_store[client_ip]
        
        if current_time - window["window_start"] > WINDOW_SECONDS:
            window["count"] = 1
            window["window_start"] = current_time
        else:
            window["count"] += 1
            
            if window["count"] > RATE_LIMIT:
                return JSONResponse(
                    status_code=429,
                    content={"detail": "Too Many Requests"},
                    headers={"Retry-After": str(WINDOW_SECONDS)}
                )
    
    response = await call_next(request)
    return response


# resource endpoint with ETag and Cache-Control

@app.get("/resource")
async def get_resource(request: Request):
    data = {"message": "This is a cacheable resource."}
    
    # convert dict → JSON string with consistent ordering
    json_content = json.dumps(data, sort_keys=True)
    
    # generate ETag from actual JSON
    etag = hashlib.sha256(json_content.encode("utf-8")).hexdigest()
    
    # check conditional request (handle quoted ETags)
    if_none_match = request.headers.get("if-none-match", "").strip('"')
    
    if if_none_match == etag:
        response = Response(status_code=304)
        response.headers["Cache-Control"] = "public, max-age=60"
        response.headers["ETag"] = etag
        return response
    
    # return full response
    response = Response(
        content=json_content,
        media_type="application/json"
    )
    response.headers["Cache-Control"] = "public, max-age=60"
    response.headers["ETag"] = etag
    
    return response
