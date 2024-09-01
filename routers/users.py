from uuid import UUID
from fastapi import APIRouter, status, Query
from models.user import UserModel

user_router =  APIRouter(prefix="/user", tags=["user"])

USERS = [{"id": UUID(int=i), "username": f"user{i}", "email": None, "first_name": "First", "last_name": "Last", "password": "pass", "isActive": True, "isAdmin": False} for i in range(1, 11)]

@user_router.get("/find/{user_id}", status_code=status.HTTP_200_OK)
async def find_user(user_id: UUID):
    user = next((usr for usr in USERS if usr["id"] == user_id), None)
    if not user:
        return {"message": "User not found"}
    return user

@user_router.get("/all", status_code=status.HTTP_200_OK)
async def read_users() -> list[UserModel]:
    return USERS

@user_router.post("/", status_code=status.HTTP_201_CREATED)
async def add_user(request: UserModel):
    USERS.append(request.dict())
    return {"message": "User added successfully"}