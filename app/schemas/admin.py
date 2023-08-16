from pydantic import BaseModel, EmailStr
from typing import Optional

class Adm(BaseModel):
    email: EmailStr
    password: str

class UpdateAdm(BaseModel):
    email: Optional[EmailStr] = None
    password: Optional[str] = None