from pydantic import BaseModel

class WelcomeKit_WKItem(BaseModel):
    welcome_kit_id: int
    item_id: int