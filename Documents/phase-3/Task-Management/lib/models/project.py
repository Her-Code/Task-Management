from database import Base
from sqlalchemy import Column,Integer,String
from sqlalchemy.orm import relationship

class Project(Base):
    __tablename__= 'projects'# the table name in the database

# Define the columns for the projects table
    id = Column(Integer(),primary_key=True)
    name = Column(String())
    description = Column(String())

# Establish a relationship with the Task model
    tasks = relationship('Task',back_populates='project')

    def __ref__(self):
        """Return a string representation of the Project instance."""
        return f"<Project(name={self.name})>"