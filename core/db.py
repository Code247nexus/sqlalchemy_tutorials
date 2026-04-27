from sqlalchemy import create_engine, MetaData,Table,Column,Integer,String,Float,DATETIME,insert,update,delete,select
from dotenv import load_dotenv
import os
from urllib.parse import quote_plus
load_dotenv()


class database:
    def __init__(self):
        self.flag = True
        self.meta = MetaData()
        self.stud1 = Table(
            "stud1",
            self.meta,
            Column("id",Integer,primary_key=True),
            Column("name",String),
            Column("age",Integer),
            Column("email",String,unique = True)
        )
        
    def get_connection(self):
        try:
            user=os.getenv("username")
            password= os.getenv("password")
            pwd = quote_plus(password)
            datab=os.getenv("database")
        
            engine = create_engine(f"postgresql+psycopg://{user}:{pwd}@localhost:5432/{datab}")
            print("connection established successfully")
            return engine
        except Exception as e:
            print(e)

    def create_table(self):
        engine = self.get_connection()
        self.meta.create_all(engine)

    def insert(self):
        engine = self.get_connection()
        with engine.begin()as conn:
            while True:
                enid = int(input("enter the id:"))
                enname = str(input("enter the name:"))
                enage = int(input("enter the age:"))
                enemail = str(input("enter the email:"))
                data = [{"id":enid,"name":enname,"age":enage, "email": enemail}]
                try:
                    conn.execute(insert(self.stud1),data)
                    print("data inserted succssfully")
                    control = input("do you wish to continue? (y/n): ").lower()
                    if control !='y':
                        break
                except Exception as e:
                    print(e)
#             data = [
#     {"id": 1, "name": "ravi sharma", "age": 25, "email": "ravisharma@gmail.com"},
#     {"id": 2, "name": "nandini kumari", "age": 22, "email": "kumarinandini@gmail.com"},
#     {"id": 3, "name": "kalma kumari", "age": 27, "email": "kumarikamla@gmail.com"},
#     {"id": 4, "name": "ajit doval", "age": 29, "email": "doval12@gmail.com"},
#     {"id": 5, "name": "atharv takla", "age": 26, "email": "taklaatharv@gmail.com"},
#     {"id": 6, "name": "Rohan Sharma", "age": 24, "email": "rohan.sharma@gmail.com"},
#     {"id": 7, "name": "Priya Verma", "age": 27, "email": "priya.verma@gmail.com"},
#     {"id": 8, "name": "Aman Gupta", "age": 25, "email": "aman.gupta@gmail.com"},
#     {"id": 9, "name": "Sneha Iyer", "age": 26, "email": "sneha.iyer@gmail.com"},
#     {"id": 10, "name": "Karan Mehta", "age": 28, "email": "karan.mehta@gmail.com"},
#     {"id": 11, "name": "Neha Singh", "age": 23, "email": "neha.singh@gmail.com"},
#     {"id": 12, "name": "Vikram Patel", "age": 29, "email": "vikram.patel@gmail.com"},
#     {"id": 13, "name": "Anjali Nair", "age": 24, "email": "anjali.nair@gmail.com"},
#     {"id": 14, "name": "Rahul Das", "age": 27, "email": "rahul.das@gmail.com"},
#     {"id": 15, "name": "Pooja Kapoor", "age": 26, "email": "pooja.kapoor@gmail.com"},
#     {"id": 16, "name": "Arjun Reddy", "age": 28, "email": "arjun.reddy@gmail.com"},
#     {"id": 17, "name": "Meera Joshi", "age": 25, "email": "meera.joshi@gmail.com"},
#     {"id": 18, "name": "Sahil Khan", "age": 27, "email": "sahil.khan@gmail.com"},
#     {"id": 19, "name": "Kavya Menon", "age": 23, "email": "kavya.menon@gmail.com"}
# ]
          
            
    def get_data(self):
        engine = self.get_connection()
        try:
            with engine.begin() as conn:
                result = conn.execute(self.stud1.select())
                for i in result:
                    print(i._mapping)
        except Exception as e:
            print(e)
            

    def update_data(self):
        engine = self.get_connection()
        empid = int(input("enter the emolyee id:"))
        column = str(input("enter the column to amend:"))
        valid_columns = ["name","age","email"]
    
        if column not in valid_columns:
            print(f"INVALID FIELD SELECTED ! kindly enter the valid fields(valid_columns)")
            return
        elif column == "age":
            new_value = int(input("enter the value: "))
        else: 
            new_value = str(input("enter the Value: "))

        try:
            col_obj = getattr(self.stud1.c,column)
            with engine.begin() as conn:
                conn.execute(update(self.stud1).where(self.stud1.c.id == empid).values({col_obj:new_value}))
                print("value amended successfully")
        except Exception as e:
            print(e)   



    def delete(self):
        engine = self.get_connection()
        del_id = int(input("enter the id to delete"))
        
        try:
            with engine.begin() as conn:
                    conn.execute(delete(self.stud1).where(self.stud1.c.id ==del_id))
                    print("data deleted successfully!")
        except Exception as e:
            print(e)
        
                


        


c1 = database()
# c1.get_connection()
# c1.insert()
c1.get_data()
# c1.delete()
# c1.update_data()