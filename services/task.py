from typing import List
from uuid import UUID
from sqlalchemy import select
from sqlalchemy.orm import Session, joinedload
from schemas.task import Task
from models.task import TaskModel, SearchTaskModel
from services.exception import ResourceNotFoundError, InvalidInputError


def get_tasks(db: Session, conds: SearchTaskModel) -> List[Task]:
    query = select(Task).options(joinedload(Task.user, innerjoin=True))
    
    if conds.title is not None:
        query = query.filter(Task.title.like(f"{conds.title}%"))
    if conds.user_id is not None:
        query = query.filter(Task.user_id == conds.user_id)
    
    query.offset((conds.page-1)*conds.size).limit(conds.size)
    
    return db.scalars(query).all()


def get_task_by_id(db: Session, id: UUID, /, joined_load = False) -> Task:
    query = select(Task).filter(Task.id == id)
    
    if joined_load:
        query.options(joinedload(Task.user, innerjoin=True))
    
    return db.scalars(query).first()
    

def add_new_task(db: Session, data: TaskModel) -> Task:
    task = Task(**data.dict())
    db.add(task)
    db.commit()
    db.refresh(task)
    
    return task

def update_task(db: Session, id: UUID, data: TaskModel) -> Task:
    task = get_task_by_id(db, id)

    if task is None:
        raise ResourceNotFoundError()

    task.title = data.title
    task.description = data.description
    task.due_date = data.due_date
    task.user_id = data.user_id
    task.updated_at = get_current_utc_time()
    
    db.commit()
    db.refresh(task)
    
    return task
