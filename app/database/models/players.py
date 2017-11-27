from sqlalchemy import Column, Integer, String, UniqueConstraint, ForeignKey
from sqlalchemy.orm import relationship

from app.database.base import Base


class Players(Base):
    __tablename__ = 'Players'
    __table_args__ = (
        UniqueConstraint('Id', 'Name', name='UniquePlayerNamePerID'),
    )

    id = Column('Id', Integer, primary_key=True)
    name = Column('Name', String(255), nullable=False)

    team_id = Column('TeamId', Integer, ForeignKey('Teams.Id', ondelete='CASCADE'),
                              nullable=False)
    team = relationship('Team', back_populates='players')

