from pydantic import BaseModel
from typing import Optional

class WelcomeKitItem(BaseModel):
    id: Optional[int] = None
    name: str
    image: bytes