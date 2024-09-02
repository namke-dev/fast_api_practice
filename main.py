from fastapi import FastAPI

from routers.users import user_router
from routers.tasks import router as task_router
from routers.companies import router as company_router
from routers.auth import router as auth_router


app = FastAPI()

app.include_router(user_router)
app.include_router(task_router)
app.include_router(company_router)

if auth_router:
    app.include_router(auth_router)
    
    
@app.get("/")
async def health_check():
    return "API Serivce is runing"