from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from datetime import date


class ClaimProcessItem(BaseModel):
    service_date: date
    submitted_procedure: str = Field(regex="^D\d{4}$")
    quadrant: Optional[str] = ""
    plan_group_no: str
    subscriber_no: str
    provider_npi: str = Field(min_length=10, max_length=10)
    provider_fee: float
    allowed_fee: float
    member_coinsurance: float
    member_copay: float

    class Config:
        orm_mode = True


class ClaimProcess(BaseModel):
    id: int
    net_fee: float

    class Config:
        orm_mode = True


class ClaimProcessRequest(BaseModel):
    items: List[ClaimProcessItem]

    class Config:
        orm_mode = True


class Queue(BaseModel):
    id: int
    type: str
    payload: Dict[str, Any]
