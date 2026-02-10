from pydantic import BaseModel
from typing import Dict


class InteractionCreate(BaseModel):
    note: str


class EditInteraction(BaseModel):
    interaction_id: str
    updates: Dict
