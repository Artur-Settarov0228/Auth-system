from fastapi import FastAPI

from app.database import Base, engine
from app.models import User, Task 
Base.metadata.create_all(engine)


app = FastAPI(title="Auth system")

@app.get("/")
async def home():
    return {"message": " Auth system"}
