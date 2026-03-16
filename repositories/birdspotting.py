
from fastapi import HTTPException
from sqlmodel import Session, select

from models.birdspotting import BirdSpotting, BirdSpottingCreate
from models.birds import Bird


class BirdSpottingRepository:

    def __init__(self, session: Session):
        self.session = session

    def get_all(self):
        statement = select(BirdSpotting)
        return self.session.exec(statement).all()

    def get_one(self, spotting_id: int):
        spotting = self.session.get(BirdSpotting, spotting_id)

        if not spotting:
            raise HTTPException(status_code=404, detail="Observation not found")

        return spotting

    def insert(self, payload: BirdSpottingCreate):

        bird = self.session.get(Bird, payload.bird_id)

        if not bird:
            raise HTTPException(status_code=400, detail="Bird does not exist")

        item = BirdSpotting.model_validate(payload)

        self.session.add(item)
        self.session.commit()
        self.session.refresh(item)

        return item