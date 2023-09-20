from app.schemas.welcome_kit_item import WelcomeKitItem
from pydantic import BaseModel
from typing import Optional


class WelcomeKit(BaseModel):
    id: Optional[int] = None
    name: str
    image: Optional[bytes]
    wk_items: list[WelcomeKitItem]