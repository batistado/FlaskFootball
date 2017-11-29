from sqlalchemy import Column, Integer, String, UniqueConstraint, ForeignKey, Boolean
from sqlalchemy.orm import relationship

from app.database.base import Base


class Player(Base):
    __tablename__ = 'Players'
    __table_args__ = (
        UniqueConstraint('Id', 'Name', name='UniquePlayerNamePerID'),
    )

    id = Column('Id', Integer, primary_key=True)
    name = Column('Name', String(255), nullable=False)
    age = Column('Age', Integer, nullable=False)
    rating = Column('Rating', Integer, nullable=False)
    starter = Column('Starter', Boolean, nullable=False)

    team_id = Column('TeamId', Integer, ForeignKey('Teams.Id', ondelete='CASCADE'), nullable=False)
    team = relationship('Team', back_populates='players')

    position_id = Column('PositionId', Integer, ForeignKey('Positions.Id'), nullable=False)
    position = relationship('Position')


