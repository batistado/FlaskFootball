from sqlalchemy import Column, Integer, String, UniqueConstraint
from sqlalchemy.orm import relationship

from app.database.base import Base


class Team(Base):
    __tablename__ = 'Teams'
    __table_args__ = (
        UniqueConstraint('Name', name='UniqueTeamName'),
    )

    id = Column('Id', Integer, primary_key=True)
    name = Column('Name', String(255), nullable=False)
    stadium = Column('Stadium', String(255))
    location = Column('Location', String(255))
    manager = Column('Manager', String(255))
    logo = Column('Logo', String(255))

    players = relationship('Player', back_populates='team', cascade='all,delete', passive_deletes=True)

