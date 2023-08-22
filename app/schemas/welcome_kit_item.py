from pydantic import BaseModel
from typing import Optional

class WelcomeKitItem(BaseModel):
    name: str
    image: bytes