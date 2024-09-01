from uuid import UUID
from fastapi import APIRouter, status, Query
from models.task import TaskModel

task_router =  APIRouter(prefix="/task", tags=["task"])

TASKS = [{"id": UUID(int=i), "summary": f"Task {i}", "description": None, "status": "Pending", "priority": i} for i in range(1, 11)]

# Task Router
@task_router.get("/find/{task_id}", status_code=status.HTTP_200_OK)
async def find_task(task_id: UUID):
    task = next((task for task in TASKS if task["id"] == task_id), None)
    if not task:
        return {"message": "Task not found"}
    return task

@task_router.get("/all", status_code=status.HTTP_200_OK)
async def read_tasks() -> list[TaskModel]:
    return TASKS

@task_router.post("/", status_code=status.HTTP_201_CREATED)
async def add_task(request: TaskModel):
    TASKS.append(request.dict())
    return {"message": "Task added successfully"}