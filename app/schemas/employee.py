from datetime import date
from enum import Enum
from pydantic import BaseModel, Field, EmailStr
from typing import Optional

class LevelAccessEnum(str, Enum):
    admin = 'admin'
    manager = 'manager'
    default = 'default'

class StatusEnum(str, Enum):
    to_be_send = 'to_be_send'
    sended = 'sended'
    delivered = 'delivered'

class Employee(BaseModel):
    first_name: str
    surname: str
    birthdate: date
    employee_role: str
    email: EmailStr
    employee_password: str
    phone_number: Optional[str] = Field(pattern=r"^(?:(?:\+|00)?(55)\s?)?(?:\(?([1-9][0-9])\)?\s?)?(?:((?:9\d|[2-9])\d{3})\-?(\d{4}))$")
    cpf: str = Field(pattern=r"^([0-9]){3}\.?([0-9]){3}\.?([0-9]){3}-?([0-9]){2}$")
    level_access: LevelAccessEnum = LevelAccessEnum.default
    company_id: int
    address_id: int

class EmployeeUpdate(BaseModel):
    first_name: Optional[str]
    surname: Optional[str]
    birthdate: Optional[date]
    employee_role: Optional[str]
    email: Optional[EmailStr]
    employee_password: Optional[str]
    phone_number: Optional[str] = Field(pattern=r"^(?:(?:\+|00)?(55)\s?)?(?:\(?([1-9][0-9])\)?\s?)?(?:((?:9\d|[2-9])\d{3})\-?(\d{4}))$")
    cpf: Optional[str] = Field(pattern=r"^([0-9]){3}\.?([0-9]){3}\.?([0-9]){3}-?([0-9]){2}$")
    level_access: Optional[LevelAccessEnum] = LevelAccessEnum.default
    company_id: Optional[int]
    address_id: Optional[int]

class EmployeeUpdateInfo(BaseModel):
    first_name: Optional[str]
    surname: Optional[str]
    cpf: Optional[str] = Field(pattern=r"^([0-9]){3}\.?([0-9]){3}\.?([0-9]){3}-?([0-9]){2}$")
    birthdate: Optional[date]
    employee_role: Optional[str]
    email: Optional[EmailStr]
    phone_number: Optional[str] = Field(pattern=r"^(?:(?:\+|00)?(55)\s?)?(?:\(?([1-9][0-9])\)?\s?)?(?:((?:9\d|[2-9])\d{3})\-?(\d{4}))$")
    zipcode: Optional[str] = Field(pattern=r'^\d{5}\-?\d{3}$')
    state: Optional[str]
    city: Optional[str]
    street: Optional[str]
    num: Optional[str]
    complement: Optional[str]
    tracking_code: Optional[str]
    status: Optional[StatusEnum]

class EmployeeUpdateLogin(BaseModel):
    email: Optional[EmailStr]
    employee_password: Optional[str]