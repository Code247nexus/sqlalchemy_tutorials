from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
import os
from urllib.parse import quote_plus
from dotenv import load_dotenv

load_dotenv()

class Database:
    def __init__(self):
        user = os.getenv("user")
        password = os.getenv("password")
        database = os.getenv("database")

        if not all([user, password, database]):
            raise ValueError("Missing environment variables!")

        pwd = quote_plus(password)

        self.engine = create_engine(
            f"postgresql+psycopg2://{user}:{pwd}@localhost:5432/{database}",
            echo=True
        )

        self.SessionLocal = sessionmaker(bind=self.engine)
        self.Base = declarative_base()

    def get_session(self):
        return self.SessionLocal()

    def get_base(self):
        return self.Base



db = Database()
Base = db.get_base()