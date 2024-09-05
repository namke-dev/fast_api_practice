from typing import Optional
from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from uuid import UUID
from models.user import UserCreateModel, UserUpdateModel, SearchUserModel, UserViewModel
from services.user import get_users, get_user_by_id, add_new_user, update_user_service, authenticate_user, create_access_token
from database.get_db import *


router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/", status_code=status.HTTP_200_OK, response_model=list[UserViewModel])
def list_users(
    username: Optional[str] = None,
    company_id: Optional[UUID] = None,
    page: int = 1,
    size: int = 10,
    db: Session = Depends(get_db_context)
):
    conds = SearchUserModel(username=username, company_id=company_id, page=page, size=size)
    users = get_users(db, conds)
    return users

@router.get("/{user_id}", status_code=status.HTTP_200_OK, response_model=UserViewModel)
def read_user(user_id: UUID, db: Session = Depends(get_db_context)):
    user = get_user_by_id(db, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.post("/", status_code=status.HTTP_200_OK, response_model=UserViewModel)
def create_user(data: UserCreateModel, db: Session = Depends(get_db_context)):
    user = add_new_user(db, data)
    return user

@router.put("/{user_id}", status_code=status.HTTP_200_OK, response_model=UserViewModel)
def update_user(user_id: UUID, data: UserUpdateModel, db: Session = Depends(get_db_context)):
    user = update_user_service(db, user_id, data)  # This line is causing recursion
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user