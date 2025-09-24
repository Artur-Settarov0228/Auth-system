from fastapi import FastAPI


from .models import User, Task
from .database import Base, engine
from .routers import router

app = FastAPI(title="Auth system")

Base.metadata.create_all(engine)
app.include_router(router)




@app.get("/")
async def home():
    return {"message": "Auth system"}