from pydantic import BaseModel, Field
from typing import Optional

class Address(BaseModel):
    num: str
    complement: Optional[str]
    zipcode: str = Field(pattern=r'^\d{5}\-?\d{3}$')
    street: str
    district: str
    city: str
    state: str

class AddressUpdate(BaseModel):
    num: Optional[str]
    complement: Optional[str]
    zipcode: Optional[str] = Field(pattern=r'^\d{5}\-?\d{3}$')
    street: Optional[str]
    district: Optional[str]
    city: Optional[str]
    state: Optional[str]