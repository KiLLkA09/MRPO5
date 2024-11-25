from sqlalchemy.orm import Session
from repository.abstract_repository import AbstractRepository

class SQLAlchemyRepository(AbstractRepository):
    def __init__(self, session: Session, model):
        self.session = session
        self.model = model

    def add(self, entity):
        self.session.add(entity)
        self.session.commit()

    def get_by_id(self, entity_id):
        return self.session.query(self.model).filter_by(id=entity_id).first()

    def get_all(self):
        return self.session.query(self.model).all()

    def delete(self, entity_id):
        entity = self.get_by_id(entity_id)
        if entity:
            self.session.delete(entity)
            self.session.commit()

    def update(self, entity):
        self.session.merge(entity)
        self.session.commit()
