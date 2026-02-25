from sqlalchemy import create_engine
SQLALCHEMY_DATABASE_URL ="postgresql://postgres:35@localhost:5432/pandas"
engine = create_engine(SQLALCHEMY_DATABASE_URL)