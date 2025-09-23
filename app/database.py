from sqlalchemy import create_engine,URL
from app.config import settings
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

url = URL.create(
    drivername="postgresql+psycopg2",
    username =settings.DB_USER,
    password=settings.DB_PASSWORD,
    host=settings.DB_HOST,
    port=settings.DB_PORT,
    database=settings.DB_NAME,
)
engine = create_engine(url, echo=True)
Base = declarative_base()
LocalSession = sessionmaker(engine)


def get_db():
    db = LocalSession()

    return db