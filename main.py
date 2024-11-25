import os
from fastapi import FastAPI, HTTPException, APIRouter, Depends, Request
from typing import Optional
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Create FastAPI instance
app = FastAPI()

# Fetch API Key from environment variables
API_KEY = os.getenv("LAB4_API_KEY")

# Function to verify API Key for request authorization
def validate_api_key(request: Request):
    provided_key = request.headers.get("G-C-P-KEY")
    if provided_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")
    return provided_key

# In-memory database simulation for tasks
tasks_collection = [
    {"id": 1, "title": "Create Lab 4", "description": "Complete Laboratory Activity 4", "completed": False}
]

# Task schema definition for validation
class TaskInput(BaseModel):
    title: str
    description: Optional[str] = ""
    completed: bool = False

# API Version 1 Router
v1_router = APIRouter()

@v1_router.get("/{task_id}")  # Modify this line to get the task directly using task_id in the URL path
def get_task_v1(task_id: int, api_key: str = Depends(validate_api_key)):
    task = next((t for t in tasks_collection if t["id"] == task_id), None)
    if not task:
        raise HTTPException(status_code=404, detail=f"Task ID {task_id} not found.")
    return task

@v1_router.post("/")  # Modify this to use the root URL for creating tasks
def create_task_v1(task: TaskInput, api_key: str = Depends(validate_api_key)):
    task_id = len(tasks_collection) + 1
    new_task = task.dict()
    new_task["id"] = task_id
    tasks_collection.append(new_task)
    return JSONResponse(status_code=201, content={"message": "New task added successfully.", "task": new_task})

@v1_router.patch("/{task_id}")  # Modify this line to update task by task_id in the URL path
def update_task_v1(task_id: int, task: TaskInput, api_key: str = Depends(validate_api_key)):
    existing_task = next((t for t in tasks_collection if t["id"] == task_id), None)
    if not existing_task:
        raise HTTPException(status_code=404, detail=f"Task ID {task_id} not found.")
    existing_task.update(task.dict())
    return JSONResponse(status_code=204)

@v1_router.delete("/{task_id}")  # Modify this line to delete task by task_id in the URL path
def delete_task_v1(task_id: int, api_key: str = Depends(validate_api_key)):
    task = next((t for t in tasks_collection if t["id"] == task_id), None)
    if not task:
        raise HTTPException(status_code=404, detail=f"Task ID {task_id} not found.")
    tasks_collection.remove(task)
    return JSONResponse(status_code=204)

# API Version 2 Router
v2_router = APIRouter()

@v2_router.get("/{task_id}")  # Modify this line to get the task directly using task_id in the URL path
def get_task_v2(task_id: int, api_key: str = Depends(validate_api_key)):
    task = next((t for t in tasks_collection if t["id"] == task_id), None)
    if not task:
        raise HTTPException(status_code=404, detail=f"Task ID {task_id} not found.")
    return task

@v2_router.post("/")  # Modify this to use the root URL for creating tasks
def create_task_v2(task: TaskInput, api_key: str = Depends(validate_api_key)):
    task_id = len(tasks_collection) + 1
    new_task = task.dict()
    new_task["id"] = task_id
    tasks_collection.append(new_task)
    return JSONResponse(status_code=201, content={"message": "Task successfully created.", "task": new_task})

@v2_router.patch("/{task_id}")  # Modify this line to update task by task_id in the URL path
def update_task_v2(task_id: int, task: TaskInput, api_key: str = Depends(validate_api_key)):
    existing_task = next((t for t in tasks_collection if t["id"] == task_id), None)
    if not existing_task:
        raise HTTPException(status_code=404, detail=f"Task ID {task_id} not found.")
    existing_task.update(task.dict())
    return JSONResponse(status_code=204)

@v2_router.delete("/{task_id}")  # Modify this line to delete task by task_id in the URL path
def delete_task_v2(task_id: int, api_key: str = Depends(validate_api_key)):
    task = next((t for t in tasks_collection if t["id"] == task_id), None)
    if not task:
        raise HTTPException(status_code=404, detail=f"Task ID {task_id} not found.")
    tasks_collection.remove(task)
    return JSONResponse(status_code=204)

# Include routers for versioned API endpoints
app.include_router(v1_router, prefix="/apiv1")
app.include_router(v2_router, prefix="/apiv2")

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome! Use /apiv1 or /apiv2 for versioned API access."}

# Health check endpoint
@app.get("/health")
def health_check():
    return {"status": "API is up and running"}
