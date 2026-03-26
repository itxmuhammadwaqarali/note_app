import uuid
from sqlalchemy import Column, String, ForeignKey, Boolean
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.database import Base

class Todo(Base):
    __tablename__ = "todos"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    title = Column(String)
    task = Column(String, default="")
    completed = Column(Boolean, default=False)
    owner_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))

    owner = relationship("User", back_populates="todos")
