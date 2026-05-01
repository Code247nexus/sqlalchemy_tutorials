from tables import create_table_column
from repository.emp_repository import CrudOperations

class CLI:

    def __init__(self):
        create_table_column()
        self.repo = CrudOperations()
        self.menu()

    def menu(self):
        while True:
            choice = input("""
1. Create Employee
2. Get Employee by ID
3. Get All Employees
4. Update Employee
5. Delete Employee
6. Exit
Choice: """)

            if choice == "1":
                self.repo.create()
            elif choice == "2":
                self.repo.retrieve_one()
            elif choice == "3":
                self.repo.retrieve_all()
            elif choice == "4":
                self.repo.update()
            elif choice == "5":
                self.repo.delete()
            elif choice == "6":
                print("Exiting...")
                break
            else:
                print("Invalid choice")


if __name__ == "__main__":
    CLI()