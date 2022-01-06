from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine=create_engine("postgresql://postgres:1234@localhost/fastapi_test",
    echo=True
)

Base=declarative_base()

SessionLocal=sessionmaker(bind=engine)