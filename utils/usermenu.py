from database.connection import DatabaseConnection
from user.flights import Flights
from user.changPswd import ChangePassword
from user.buyTicket import BuyTicket
from user.myTicket import MyTicket
from user.cancelTicket import TicketCancel
from session.sessionManager import session

def user_menu():
    db = DatabaseConnection()
    db.connect()

    while True:

        print("\n=== Passenger MENU ===")
        print("1. Check Flights Schedule 📅")
        print("2. Buy Ticket")
        print("3. My Booked Tickets")
        print("4. Cancel Ticket")
        print("5. Change Password")
        print("6. Exit!")


        choice = input("\n Enter your choice: ")

        if choice == "1":
            print("\n Checks Flight schedule:")
            Flights()

        elif choice == "2":
            print("\n Buy Ticket!")
            BuyTicket()
        
        elif choice == "3":
            print("\n My Booked Tickets!")
            MyTicket()
        
        elif choice == "4":
            print("\n Cancel Ticekt!")
            TicketCancel()

        elif choice == "5":
            print("\n Change Password!")
            ChangePassword()

        
        elif choice == "6":
            print("👋 Exiting the system. Goodbye!")
            session.clear_user()
            db.close()
            break

        else:
            print("\n ❌ Invalid choice! Try again.")