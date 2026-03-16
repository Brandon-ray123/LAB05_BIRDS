
from typing import Optional
from datetime import datetime
from sqlmodel import Field, Relationship, SQLModel
from models.birds import Bird


class BirdSpottingBase(SQLModel):
    spotted_at: datetime
    location: str
    observer_name: str
    notes: Optional[str] = None


class BirdSpotting(BirdSpottingBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    bird_id: int = Field(foreign_key="bird.id")
    bird: Optional[Bird] = Relationship()


class BirdSpottingCreate(BirdSpottingBase):
    bird_id: int