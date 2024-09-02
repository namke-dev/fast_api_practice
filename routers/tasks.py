from typing import List
from uuid import UUID
from fastapi import APIRouter, status, Depends, Query
from sqlalchemy.orm import Session

from database.get_db import get_db_context
from models.user import UserClaims
from services import task as TaskService
from services.exception import ResourceNotFoundError
from models.task import TaskModel, TaskViewModel, SearchTaskModel
from services.auth import authorizer

router = APIRouter(prefix="/tasks", tags=["Tasks"])

@router.get("", status_code=status.HTTP_200_OK, response_model=List[TaskViewModel])
async def get_all_tasks(
    title: str = Query(default=None),
    user_id: UUID = Query(default=None),
    page: int = Query(ge=1, default=1),
    size: int = Query(ge=1, le=50, default=10),
    db: Session = Depends(get_db_context),
    user: UserClaims = Depends(authorizer),
):
    conds = SearchTaskModel(user_id=user_id if user.isAdmin else user.sub, page=page, size=size)
    return TaskService.get_tasks(db, conds, user.isAdmin)

@router.post("", status_code=status.HTTP_201_CREATED, response_model=TaskViewModel)
async def create_task(
    request: TaskModel, 
    db: Session = Depends(get_db_context),
    user: UserClaims = Depends(authorizer),
):  
    request.owner_id = UUID(user.sub)
    return TaskService.add_new_task(db, request)

@router.get("/{task_id}", response_model=TaskViewModel)
async def get_task_detail(task_id: UUID, db: Session=Depends(get_db_context), user: UserClaims = Depends(authorizer)):
    task = TaskService.get_task_by_id(db, task_id)

    if task is None or (not user.isAdmin and task.owner_id != UUID(user.sub)):
        raise ResourceNotFoundError()

    return task

@router.put("/{task_id}", status_code=status.HTTP_200_OK, response_model=TaskViewModel)
async def update_task(
    task_id: UUID,
    request: TaskModel,
    db: Session=Depends(get_db_context),
    user: UserClaims = Depends(authorizer),
):
    return TaskService.update_task(db, task_id, request, user.isAdmin)
