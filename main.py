from fastapi import FastAPI

from routers.users import user_router
from routers.tasks import task_router
from routers.companies import company_router

app = FastAPI()

app.include_router(user_router)
app.include_router(task_router)
app.include_router(company_router)

@app.get("/")
async def health_check():
    return "API Serivce is runing"