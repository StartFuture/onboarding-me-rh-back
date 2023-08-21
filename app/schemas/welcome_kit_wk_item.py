from pydantic import BaseModel
from typing import Optional

class WelcomeKit_WKItem(BaseModel):
    welcome_kit_id: int
    item_id: int