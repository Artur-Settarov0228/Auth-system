from sqlalchemy import Column, Integer, String, Boolean, Text, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class User(Base):
    __tablename__ = "users"
    user_id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(70), nullable=False)
    last_name = Column(String(100), nullable=False)
    email = Column(String(300), unique=True, index=True, nullable=False)
    hashed_password = Column(String(300), nullable=False)
    is_active = Column(Boolean, default=True)
    is_verified = Column(Boolean, default=False)
    verification_code = Column(Integer) 

    tasks = relationship("Task", back_populates="user")
    

@property
def ful_name(self):
    if self.firist_name:
        return f"{self.firist_name} {self.last_name}"
    else:
        return self.last_name
def __repr__(self):
     return f"{self.user_id}: {self.email}- {self.user.ful_name}"
    

class Task(Base):
    __tablename__ = "tasks"
    task_id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    description = Column(Text, nullable=True)
    user_name = Column(ForeignKey("users.user_id"), onupdate="CASCADE"),
   

    user = relationship("User", back_populates="tasks")

    def __repr__(self):
        return f"{self.task_id}: {self.title}- {self.user.ful_name}"
    



