from fastapi import FastAPI
from app.tasks.example import add_task

app = FastAPI(title="Async Event System")

@app.get("/")
def root():
    return {"message": "Async system running"}

@app.post("/add")
def add(a: int, b: int):
    task = add_task.delay(a, b)
    return {"task_id": task.id}
