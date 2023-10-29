from typing import Union
from schemas import *
from fastapi import FastAPI

app = FastAPI()

tasks: list[Task] = []


@app.get("/")
def read_root():
    return {"Hello": "World!"}


@app.get("/ping")
async def ping_pong():
    return {"answer": "pong"}


@app.get("/tasks", response_model=list[Task])
async def read_item():
    return tasks


@app.post("/tasks")
async def read_item(task: Task):
    tasks.append(task)
