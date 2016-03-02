from sqlalchemy import Column, Integer, Text, Boolean
from sqlalchemy.orm import relationship
from repositories.config import Base


class ComputerTable(Base):
    __tablename__ = "computers"

    id = Column(Integer, primary_key=True)
    model = Column(Text, index=True, unique=True)    # The model name
    bits = Column(Integer)
    ram = Column(Integer)                            # In Kilobytes, we go vintage
    rom = Column(Integer, nullable=True)
    programs = relationship("Program", backref="made_for",
                            cascade="all, delete, delete-orphan")  # A computer can have many programs

    def __repr__(self):
        return "repositories.ComputerTable: {}".format(self.model)
