from database.connection import DatabaseConnection
from user.signup import Signup
from user.login import Login
from session.sessionManager import session


def main_menu():
    try:
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
                print("👋 Exiting the system. Goodbye!")
                session.clear_user()
                db.close()
                break
            else:
                print(" Invalid choice! Try again.")
    except Exception as e:
        print("⚠️ Unexpected Error:", e)