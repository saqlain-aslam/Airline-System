
from database.connection import DatabaseConnection

def main_menu():
    db = DatabaseConnection()
    db.connect()
  
    cursor = db.get_cursor()

    while True:
        print("\n=== MAIN MENU ===")
        print("1. Login")
        print("2. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            print(" (Login functionality will come next)")

            cursor.execute("SELECT * FROM users")
            rows = cursor.fetchall()
            for row in rows:
                print(row)

        elif choice == "2":
            print(" Exiting the system. Goodbye!")
            db.close()
            break
        else:
            print(" Invalid choice! Try again.")
