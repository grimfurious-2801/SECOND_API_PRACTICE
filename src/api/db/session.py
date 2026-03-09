import sqlmodel

from sqlmodel import SQLModel

from .config import DATABASE_URL

if DATABASE_URL == "":
    raise NotImplementedError("DATABASE_URL need to be set")

engine = sqlmodel.create_engine(DATABASE_URL, echo=True)

def init_db():
    print('creating database')
    SQLModel.metadata.create_all(engine)

# from sqlalchemy import create_engine, text

# CONNECTION = "timescaledb://tsdbadmin:n1lz9wz90m4avdiu@my2oashliv.mpor6xgixq.tsdb.cloud.timescale.com:36852/tsdb"

# engine = create_engine(CONNECTION)
# with engine.connect() as conn:
#     cursor = conn.execute(text('select extname, extversion from pg_extension;'))
#     for extension in cursor:
#         print(extension)