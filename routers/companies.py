from uuid import UUID
from fastapi import APIRouter, status, Query
from models.company import CompanyModel

company_router = APIRouter(prefix="/companies", tags=["companies"])

COMPANIES = [{"id": UUID(int=i), "name": f"Company {i}", "description": None, "mode": "mode", "rating": i} for i in range(1, 11)]


# Company Router
@company_router.get("/find/{company_id}", status_code=status.HTTP_200_OK)
async def find_company(company_id: UUID):
    company = next((comp for comp in COMPANIES if comp["id"] == company_id), None)
    if not company:
        return {"message": "Company not found"}
    return company

@company_router.get("/all", status_code=status.HTTP_200_OK)
async def read_companies() -> list[CompanyModel]:
    return COMPANIES

@company_router.post("/", status_code=status.HTTP_201_CREATED)
async def add_company(request: CompanyModel):
    COMPANIES.append(request.dict())
    return {"message": "Company added successfully"}
