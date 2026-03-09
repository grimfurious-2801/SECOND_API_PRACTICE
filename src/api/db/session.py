import sqlmodel

from sqlmodel import SQLModel

from .config import DATABASE_URL

if DATABASE_URL == "":
    raise NotImplementedError("DATABASE_URL need to be set")

engine = sqlmodel.create_engine(DATABASE_URL, echo=True)

def init_db():
    print('creating database')
    SQLModel.metadata.create_all(engine)

