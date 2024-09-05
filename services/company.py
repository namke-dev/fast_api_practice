import uuid
from uuid import UUID
from sqlalchemy import select
from sqlalchemy.orm import Session
from schemas.company import Company
from models.company import CompanyModel, SearchCompanyModel, CompanyCreateModel
from services.utils import get_current_utc_time
from services.exception import ResourceNotFoundError, InvalidInputError

def get_companies(db: Session, conds: SearchCompanyModel):
    query = select(Company)
    
    if conds.name:
        query = query.filter(Company.name.like(f"{conds.name}%"))
    if conds.mode:
        query = query.filter(Company.mode == conds.mode)
    
    query.offset((conds.page-1) * conds.size).limit(conds.size)
    
    return db.scalars(query).all()

def get_company_by_id(db: Session, id: UUID):
    query = select(Company).filter(Company.id == id)
    
    return db.scalars(query).first()

def add_new_company(db: Session, data: CompanyCreateModel) -> Company:
    company = Company(
        name=data.name,
        description=data.description,
        mode=data.mode,
        rating=data.rating
    )
    company.created_at = get_current_utc_time()
    company.updated_at = get_current_utc_time()

    db.add(company)
    db.commit()
    db.refresh(company)
    
    return company

def update_company(db: Session, id: UUID, data: CompanyModel) -> Company:
    company = get_company_by_id(db, id)

    if company is None:
        raise ResourceNotFoundError()

    company.name = data.name
    company.description = data.description
    company.mode = data.mode
    company.rating = data.rating
    company.updated_at = get_current_utc_time()
    
    db.commit()
    db.refresh(company)
    
    return company
