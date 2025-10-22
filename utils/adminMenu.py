from database.connection import DatabaseConnection
from user.flights import Flights

def user_menu():
    db = DatabaseConnection()
    db.connect()

    while True:

        print("\n=== Admin MENU ===")
        print("1. Check Flights Schedule 📅")
        print("2. Add new Route")
        print("3. Remove Existing Route")
        print("4. Add new Plane")
        print("5. Remove Plane")
        print("6. Exit!")

        choice = input("\n Enter your choice: ")

        if choice == "1":
            print("\n Checks Flight schedule:")
            Flights()

        elif choice == "2":
            print("\n Add new Route")
        
        elif choice == "3":
            print("\n Remove Existing Route")
        
        elif choice == "4":
            print("\n Add new Plane")

        elif choice == "5":
            print("\n Remove Plane")
        
        elif choice == "6":
            print("👋 Exiting the system. Goodbye!")
            db.close()
            break

        else:
            print("\n ❌ Invalid choice! Try again.")