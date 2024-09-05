from typing import List
from uuid import UUID
from fastapi import APIRouter, status, Depends, Query
from sqlalchemy.orm import Session

from database.get_db import *
from models.user import UserClaims
from services import company as CompanyService
from services.exception import *
from models.company import CompanyModel, CompanyViewModel, SearchCompanyModel, CompanyCreateModel
from services.auth import authorizer

router = APIRouter(prefix="/companies", tags=["Companies"])

@router.get("", status_code=status.HTTP_200_OK, response_model=List[CompanyViewModel])
async def get_all_companies(
    name: str = Query(default=None),
    mode: str = Query(default=None),
    page: int = Query(ge=1, default=1),
    size: int = Query(ge=1, le=50, default=10),
    db: Session = Depends(get_db_context),
):
    conds = SearchCompanyModel(name=name, mode=mode, page=page, size=size)
    return CompanyService.get_companies(db, conds)

@router.post("", status_code=status.HTTP_201_CREATED, response_model=CompanyViewModel)
async def create_company(
    request: CompanyCreateModel, 
    db: Session = Depends(get_db_context),
):
    return CompanyService.add_new_company(db, request)

@router.get("/{company_id}", response_model=CompanyViewModel)
async def get_company_detail(
    company_id: UUID, 
    db: Session = Depends(get_db_context),
):
    company = CompanyService.get_company_by_id(db, company_id)
    
    if company is None:
        raise ResourceNotFoundError()

    return company

@router.put("/{company_id}", status_code=status.HTTP_200_OK, response_model=CompanyViewModel)
async def update_company(
    company_id: UUID,
    request: CompanyModel,
    db: Session = Depends(get_db_context),
):
    return CompanyService.update_company(db, company_id, request)
