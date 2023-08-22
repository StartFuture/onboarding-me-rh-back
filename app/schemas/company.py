from fastapi import Query
from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Company(BaseModel):
    company_name: str
    trading_name: str
    logo: Optional[bytes]
    cnpj: str = Field(pattern=r'^\d{2}\.?\d{3}\.?\d{3}\/?\d{4}\-?\d{2}$')
    email: EmailStr
    company_password: str
    state_register: Optional[str] = Query(..., max_length=14)

class CompanyUpdate(BaseModel):
    company_name: Optional[str]
    trading_name: Optional[str]
    logo: Optional[bytes]
    cnpj: Optional[str] = Field(pattern=r'^\d{2}\.?\d{3}\.?\d{3}\/?\d{4}\-??\d{2}$')
    email: Optional[EmailStr]
    company_password: Optional[str]
    state_register: Optional[str] = Query(..., max_length=14)

class CompanyUpdateLogin(BaseModel):
    email: Optional[EmailStr]
    company_password: Optional[str]