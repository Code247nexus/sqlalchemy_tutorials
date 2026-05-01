from core.database import db
from models.models1 import Employee

class CrudOperations:

    def create(self):
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        department = input("Enter department: ")

        session = db.get_session()
        try:
            emp = Employee(name=name, age=age, department=department)
            session.add(emp)
            session.commit()
            print("Employee created:", emp)
        finally:
            session.close()

    def update(self):
        session = db.get_session()
        try:
            emp_id = int(input("Enter employee ID: "))
            field = input("Field (name, age, department): ")

            if field not in ["name", "age", "department"]:
                print("Invalid field")
                return

            value = int(input("New value: ")) if field == "age" else input("New value: ")

            emp = session.query(Employee).filter_by(id=emp_id).first()

            if not emp:
                print("Employee not found")
                return

            setattr(emp, field, value)
            session.commit()

            print("Updated:", emp)

        finally:
            session.close()

    def retrieve_one(self):
        session = db.get_session()
        try:
            emp_id = int(input("Enter ID: "))
            emp = session.query(Employee).filter_by(id=emp_id).first()

            if emp:
                print(emp)
            else:
                print("Employee not found")

        finally:
            session.close()

    def retrieve_all(self):
        session = db.get_session()
        try:
            employees = session.query(Employee).all()

            if not employees:
                print("No records found")
                return

            for emp in employees:
                print(emp)

        finally:
            session.close()

    def delete(self):
        session = db.get_session()
        try:
            emp_id = int(input("Enter ID to delete: "))
            emp = session.query(Employee).filter_by(id=emp_id).first()

            if not emp:
                print("Employee not found")
                return

            session.delete(emp)
            session.commit()
            print("Deleted successfully")

        finally:
            session.close()