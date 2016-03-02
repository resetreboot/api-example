from sqlalchemy import Column, Integer, Text, Boolean
from repositories.config import Base


class ProgramTable(Base):
    __tablename__ = "programs"

    id = Column(Integer, primary_key=True)
    name = Column(Text, index=True)    # The program name
    version = Column(Text)

    def __repr__(self):
        return "repositories.ProgramTable: {0} v{1}".format(self.name, self.version)
