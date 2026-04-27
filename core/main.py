from db import database

class main:
    def __init__(self):
        self.d1 = database()
        self.menu()
    def menu(self):
        while True:
            print("hii this is sqlalchemy tuorial with cli based application")
            user_input = input("""HOW WOULD YOU LIK TO PROCEED:
                               1)INSERT THE DATA
                               2)VIEW THE DATA
                               3)UPDATE THE DATA
                               4)DELETE
                               5)EXIT
                               """)
            if user_input == '1':
                self.d1.insert()
            elif user_input == '2':
                self.d1.get_data()
            elif user_input =='3':
                self.d1.update_data()
            elif user_input =='4':
                self.d1.delete()
            else:
                exit()


c1 = main()