
from database.connection import DatabaseConnection
from models.signup import Signup
from models.login import Login


def main_menu():
    db = DatabaseConnection()
    db.connect()
  
    cursor = db.get_cursor()

    while True:

        print("\n=== MAIN MENU ===")
        print("1. Signup")
        print("2. Login")
        print("3. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            print("\n Signup Form:")
            Signup()

            # cursor.execute("SELECT name,email, gender FROM users")
            # rows = cursor.fetchall()
            # for row in rows:
            #     print(row)


        elif choice == "2":
            print("\n Login Form:")
            Login()

        elif choice == "3":
            print(" Exiting the system. Goodbye!")
            db.close()
            break
        else:
            print(" Invalid choice! Try again.")
