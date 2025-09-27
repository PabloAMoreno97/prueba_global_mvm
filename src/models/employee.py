from utils.constants import Department, Role
from sqlalchemy import Column, Integer, String

from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Employee(Base):

    __tablename__ = "employees"

    id = Column(Integer, primary_key=True)
    role = Column(String(100), nullable=False)
    department = Column(String(50), nullable=False)

    def __init__(self, id: int, role: Role, department: Department):
        self.id = id
        self.role = role.name
        self.department = department.name

    def __repr__(self):
        return f"{self.id} - {self.role} - {self.department}"

    def to_tuple(self):
        return (self.id, self.role, self.department)
