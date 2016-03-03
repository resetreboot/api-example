from sqlalchemy import Column, Integer, Text, Boolean, ForeignKey
from repositories.config import Base
from sqlalchemy.orm import relationship


class ProgramTable(Base):
    __tablename__ = "programs"

    id = Column(Integer, primary_key=True)
    name = Column(Text, index=True)    # The program name
    version = Column(Text)
    computer_id = Column(Integer, ForeignKey('computers.id'))
    made_for = relationship("ComputerTable", back_populates="programs")

    def __repr__(self):
        return "repositories.ProgramTable: {0} v{1}".format(self.name, self.version)
