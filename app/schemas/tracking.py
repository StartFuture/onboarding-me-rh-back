from pydantic import BaseModel
from typing import Optional
from enum import Enum

class StatusEnum(str, Enum):
    to_be_send = 'to_be_send'
    sended = 'sended'
    delivered = 'delivered'

class Tracking(BaseModel):
    tracking_code: str = "tracking"
    status: StatusEnum = StatusEnum.to_be_send
    employee_id: Optional[int] = None
    welcome_kit_id: int

class TrackingUpdate(BaseModel):
    tracking_code: Optional[str]
    status: Optional[StatusEnum]