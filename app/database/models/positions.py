from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.database.base import Base


class Position(Base):
    __tablename__ = 'Positions'
    __table_args__ = ()

    id = Column('Id', Integer, primary_key=True)
    name = Column('Name', String(255), nullable=False)

    players = relationship('Player', back_populates='position')
