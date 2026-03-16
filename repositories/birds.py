
from fastapi import HTTPException
from sqlmodel import Session, select
from models.birds import Bird, BirdCreate
from models.species import Species


class BirdRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_all(self):
        statement = select(Bird)
        return self.session.exec(statement).all()

    def insert(self, payload: BirdCreate):
        species = self.session.get(Species, payload.species_id)

        if not species:
            raise HTTPException(status_code=400, detail="Species does not exist")

        item = Bird.model_validate(payload)

        self.session.add(item)
        self.session.commit()
        self.session.refresh(item)

        return item