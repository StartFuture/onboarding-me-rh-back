from pydantic import BaseModel, EmailStr
from typing import List, Any

class EmailSchema(BaseModel):
    email: List[EmailStr]
    body: dict[str, Any]