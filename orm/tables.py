from core.database import db, Base
from models.models1 import Employee  # ✅ IMPORTANT (register model)

def create_table_column():
    print("Tables detected:", Base.metadata.tables.keys())  # debug
    Base.metadata.create_all(bind=db.engine)
    print("table created successfully")