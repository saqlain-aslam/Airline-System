import os
from dotenv import load_dotenv
from database.connection import DatabaseConnection
from utils.userMenu import user_menu
from utils.adminMenu import admin_menu
from session.sessionManager import session

def Login():

    db = DatabaseConnection()
    db.connect()
  
    cursor = db.get_cursor()

    load_dotenv()
    

    
    print("*" * 50 )
    print("\n 💻 Enter your email and password to Login! \n")
    print("*" * 50)

  
    ADMIN_EMAIL = os.getenv("ADMIN_EMAIL")
    ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD")

    email = str(input("\n Enter your email:"))
    password = str(input("\n Enter your password:"))


    if email == ADMIN_EMAIL and password == ADMIN_PASSWORD:
        print("\n 👑 Admin Login Successful!")
        print("*" * 50)
        admin_menu()
        return 
    

    sql_query = """
    SELECT id, name, email, gender FROM users WHERE email = %s AND password = %s;
    """
    
    cursor.execute(sql_query,(email, password))
    user = cursor.fetchone()
     

    if( user):
        print("\n ✔ Login Successfully!")
        print("*" * 50)

        session.set_user({
            "id": user[0],
            "name": user[1],
            "email": user[2],
        })

        user_menu()

    else:
       print("❌ Kindly enter valid credentials and If you don't have account Signup first!")



