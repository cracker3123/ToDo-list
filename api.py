from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Task(BaseModel):
    title: str
    description: str

tasks = []

@app.post("/tasks/")
async def create_task(task: Task):
    tasks.append(task)
    return {"task": task}

@app.get("/tasks/", response_model=List[Task])
async def read_tasks():
    return tasks

@app.get("/tasks/{task_id}", response_model=Task)
async def read_task(task_id: int):
    try:
        return tasks[task_id]
    except IndexError:
        raise HTTPException(status_code=404, detail="Task not found")

@app.put("/tasks/{task_id}")
async def update_task(task_id: int, task: Task):
    try:
        tasks[task_id] = task
        return {"task": task}
    except IndexError:
        raise HTTPException(status_code=404, detail="Task not found")

@app.delete("/tasks/{task_id}")
async def delete_task(task_id: int):
    try:
        task = tasks.pop(task_id)
        return {"task": task}
    except IndexError:
        raise HTTPException(status_code=404, detail="Task not found")


