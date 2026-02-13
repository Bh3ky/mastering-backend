from fastapi import FastAPI, Response, Request
from fastapi.middleware.cors import CORSMiddleware
import hashlib
import json

app = FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/resource")
def get_resource(request: Request, response: Response):
    data = {"message": "This is a cacheable resource."}

    # convert to consistent JSON string
    body = json.dumps(data, sort_keys=True)

    # generate hash
    etag = hashlib.sha256(body.encode()).hexdigest()
    formatted_etag = f'"{etag}"'

    # check conditional header
    client_etag = request.headers.get("if-none-match")

    # set headers
    response.headers["Cache-Control"] = "public, max-age=60"
    response.headers["ETag"] = formatted_etag

    if client_etag == formatted_etag:
        return Response(status_code=304, headers=response.headers)

    return data
