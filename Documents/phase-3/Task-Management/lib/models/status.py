import enum
# from sqlalchemy import Enum

class Status(enum.Enum):
    """Enumeration representing the status of a task."""
    PENDING = "pending"
    COMPLETED = "completed"

    def __repr__(self):
        """Return a string representation of the Status instance."""
        return f"<Status(status={self.name})>"
