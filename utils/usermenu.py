from database.connection import DatabaseConnection
from models.flights import Flights
from models.changpswd import ChangePassword

def user_menu():
    db = DatabaseConnection()
    db.connect()

    while True:

        print("\n=== Passenger MENU ===")
        print("1. Check Flights Schedule 📅")
        print("2. Buy Ticket")
        print("3. Cancel Ticket")
        print("4. Change Password")
        print("5. Exit!")


        choice = input("\n Enter your choice: ")

        if choice == "1":
            print("\n Checks Flight schedule:")
            Flights()


        elif choice == "2":
            print("\n Buy Ticket!")

        elif choice == "3":
            print("\n Cancel Ticekt!")
        
        elif choice == "4":
            print("\n Change Password!")
            ChangePassword()
        
        elif choice == "5":
            print("👋 Exiting the system. Goodbye!")
            db.close()
            break

        else:
            print("\n ❌ Invalid choice! Try again.")
