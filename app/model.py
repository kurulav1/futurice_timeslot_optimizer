from pydantic import BaseModel, Field, validator
from typing import List
from datetime import datetime

'''
Data models for meeting optimization API.
'''
class Participant(BaseModel):
    name: str = Field(min_length=3)
    preferredSlots: List[str] = Field(default_factory=list)

    @validator("preferredSlots", each_item=True)
    def validate_slot(cls, v):
        try:
            datetime.fromisoformat(v)
        except Exception:
            raise ValueError("Each preferred slot must be a valid ISO format datetime string (e.g., 2024-06-10T10:00)")
        return v


class SlotResult(BaseModel):
    slot: str
    participants: List[str]


class OptimizeRequest(BaseModel):
    meetingName: str = Field(min_length=3)
    participants: List[Participant] = Field(min_length=1)


class OptimizeResponse(BaseModel):
    meetingName: str
    optimalSlots: List[SlotResult]
    maxParticipants: int
