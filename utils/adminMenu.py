from database.connection import DatabaseConnection
from user.flights import Flights
from admin.addPlane import AddPlane
from admin.newRoute import AddRoute
from admin.removePlane import RemovePlane
from admin.removeRoute import RemoveRoute
from user.flights import Flights
from admin.removeUser import RemoveUser
from admin.planes import Planes
from admin.users import Users

def admin_menu():
    try:
        db = DatabaseConnection()
        db.connect()

        while True:

            print("\n=== Admin MENU ===")
            print("1. Check Flights Schedule 📅")
            print("2. Add new Route")
            print("3. Remove Existing Route")
            print("4. Add new Plane")
            print("5. Remove Plane")
            print("6. Remove User")
            print("7. Existing Planes")
            print("8. Regsitered Users")
            print("9. Exit!")

            choice = input("\n Enter your choice: ")

            if choice == "1":
                print("\n Checks Flight schedule:")
                Flights()

            elif choice == "2":
                print("\n Add new Flight")
                AddRoute()
        
            elif choice == "3":
                print("\n Remove Existing Route")
                RemoveRoute()
        
            elif choice == "4":
                print("\n Add new Plane")
                AddPlane()

            elif choice == "5":
                print("\n Remove Plane")
                RemovePlane()
            
            elif choice == "6":
                print("\n Remove User")
                RemoveUser()
            
            elif choice == "7":
                print("\n Total Planes")
                Planes()

            elif choice == "8":
                print("\n Total Users")
                Users()
        
            elif choice == "9":
                print("👋 Exiting the system. Goodbye!")
                db.close()
                break

            else:
                print("\n ❌ Invalid choice! Try again.")
    except Exception as e:
        print("⚠️ Unexpected Error:", e)