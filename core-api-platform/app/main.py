from fastapi import FastAPI

app = FastAPI(title="Core API Platform")

@app.get("/")
def read_root():
    return {"message": "Core API Platform is alive"}
