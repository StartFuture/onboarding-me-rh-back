from pydantic import BaseModel, Field


class Employee(BaseModel):
    id: str 
    name: str
    cpf: str = Field(pattern=r"^([0-9]){3}\.([0-9]){3}\.([0-9]){3}-([0-9]){2}$")