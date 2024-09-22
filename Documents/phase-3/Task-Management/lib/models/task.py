from database import Base
from sqlalchemy import Column,Integer,String,DateTime,Enum,ForeignKey
from models.status import Status
from sqlalchemy.orm import relationship

class Task(Base):
    """Model representing a task in the task management system."""
    __tablename__='tasks'# the table name in the database

    id = Column(Integer(),primary_key=True)
    title = Column(String())
    description = Column(String())
    due_date = Column(DateTime)# Due date for the task (optional)
    status = Column(Enum(Status),default = Status.PENDING)# Status of the task, default is PENDING
    project_id = Column(Integer(),ForeignKey('projects.id'))# Foreign key linking to the projects table

# Establishes a relationship with the Project model
    project = relationship("Project",back_populates="tasks")

    def __repr__(self):
        """Return a string representation of the Task instance."""
        return f"<Task(title={self.title}, status={self.status})>" # Provides a readable representation for debugging
