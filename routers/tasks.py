from typing import List
from uuid import UUID
from fastapi import APIRouter, status, Depends, Query
from sqlalchemy.orm import Session

from database.get_db import get_db_context
from models.user import UserClaims
from services import task as TaskService
from services.exception import ResourceNotFoundError
from models.task import TaskModel, TaskViewModel, SearchTaskModel, TaskUpdateModel
from services.auth import authorizer

router = APIRouter(prefix="/tasks", tags=["Tasks"])

@router.get("", status_code=status.HTTP_200_OK, response_model=List[TaskViewModel])
def list_tasks(conds: SearchTaskModel = Depends(), db: Session = Depends(get_db_context)):
    tasks = TaskService.get_tasks(db, conds)
    return tasks

@router.post("", status_code=status.HTTP_201_CREATED, response_model=TaskViewModel)
async def create_task(
    request: TaskModel, 
    db: Session = Depends(get_db_context),
):  
    # request.user_id = UUID(user.user_id)
    return TaskService.add_new_task(db, request)

@router.get("/{task_id}", response_model=TaskViewModel)
async def get_task_detail(task_id: UUID, db: Session=Depends(get_db_context)):
    task = TaskService.get_task_by_id(db, task_id)

    if task is None:
        raise ResourceNotFoundError()

    return task

@router.put("/{task_id}", status_code=status.HTTP_200_OK, response_model=TaskViewModel)
async def update_task(
    task_id: UUID,
    request: TaskUpdateModel,
    db: Session=Depends(get_db_context)
):
    return TaskService.update_task(db, task_id, request)
