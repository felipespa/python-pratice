from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

# "sqlite:///./todosapp.db"
# "mysql+pymysql://root:test1234!@127.0.0.1:3306/TodoApplicationDatabase"

SQLALCHEMY_DATABASE_URL = "sqlite:///./todosapp.db"


engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
