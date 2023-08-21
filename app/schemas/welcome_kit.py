from pydantic import BaseModel
from typing import Optional

class WelcomeKit(BaseModel):
    name: str
    image: Optional[bytes]