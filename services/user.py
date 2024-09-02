from typing import List
from uuid import UUID
from sqlalchemy import select
from sqlalchemy.orm import Session, joinedload
from schemas.user import User
from models.user import UserModel, SearchUserModel
from services.exception import ResourceNotFoundError, InvalidInputError


def get_users(db: Session, conds: SearchUserModel) -> List[User]:
    query = select(User).options(joinedload(User.company, innerjoin=True))
    
    if conds.name is not None:
        query = query.filter(User.name.like(f"{conds.name}%"))
    if conds.company_id is not None:
        query = query.filter(User.company_id == conds.company_id)
    
    query.offset((conds.page-1)*conds.size).limit(conds.size)
    
    return db.scalars(query).all()


def get_user_by_id(db: Session, id: UUID, /, joined_load = False) -> User:
    query = select(User).filter(User.id == id)
    
    if joined_load:
        query.options(joinedload(User.company, innerjoin=True))
    
    return db.scalars(query).first()
    

def add_new_user(db: Session, data: UserModel) -> User:
    user = User(**data.dict())
    db.add(user)
    db.commit()
    db.refresh(user)
    
    return user

def update_user(db: Session, id: UUID, data: UserModel) -> User:
    user = get_user_by_id(db, id)

    if user is None:
        raise ResourceNotFoundError()

    user.name = data.name
    user.email = data.email
    user.company_id = data.company_id
    user.updated_at = get_current_utc_time()
    
    db.commit()
    db.refresh(user)
    
    return user
