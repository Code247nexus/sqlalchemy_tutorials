from sqlalchemy import Column, Integer, String
from core.database import Base

class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    age = Column(Integer)
    department = Column(String)

    def __repr__(self):
        return f"Employee(id={self.id}, name={self.name}, age={self.age}, dept={self.department})"