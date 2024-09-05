from typing import List
from uuid import UUID
from sqlalchemy import select
from sqlalchemy.orm import Session, joinedload
from schemas.task import Task
from models.task import TaskModel, SearchTaskModel, TaskUpdateModel
from services.exception import ResourceNotFoundError, InvalidInputError


def get_tasks(db: Session, conds: SearchTaskModel) -> List[Task]:
    query = select(Task)

    if conds.user_id:
        query = query.filter(Task.user_id == UUID(conds.user_id))
    if conds.status:
        query = query.filter(Task.status == conds.status)
    
    # Pagination
    query = query.offset((conds.page - 1) * conds.size).limit(conds.size)

    return db.scalars(query).all()


def get_task_by_id(db: Session, id: UUID, /, joined_load = False) -> Task:
    query = select(Task).filter(Task.id == id)
    
    return db.scalars(query).first()
    

def add_new_task(db: Session, data: TaskModel) -> Task:
    task = Task(**data.dict())
    db.add(task)
    db.commit()
    db.refresh(task)
    
    return task

def update_task(db: Session, id: UUID, data: TaskUpdateModel) -> Task:
    task = get_task_by_id(db, id)

    if task is None:
        raise ResourceNotFoundError()
    
    task.summary = data.summary
    task.description = data.description
    task.status = data.status
    task.priority  = data.priority
    
    db.commit()
    db.refresh(task)
    
    return task
