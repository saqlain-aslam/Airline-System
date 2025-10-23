from database.connection import DatabaseConnection
from utils.userMenu import user_menu
from session.sessionManager import session

def Signup():

    db = DatabaseConnection()
    db.connect()
  
    cursor = db.get_cursor()
    
    print("*" * 50 )
    
    print("\n 💻 Enter your data to Signup! \n")
    print("*" * 50)

    name = str(input("\n Enter your name:"))
    email = str(input("\n Enter your email:"))
    gender = str(input("\n Enter your gender:"))
    password = str(input("\n Enter your password:"))

    if(email,gender,name,password):
        pass
    else:
        print("Kindly enter complete data")
        return
    
    
    email_query = """
    SELECT email FROM users WHERE email = %s;
    """

    cursor.execute(email_query, (email,))
    test_email = cursor.fetchall()
    
    if test_email:
        print("\n ❌ Email already exists. Please go for Login!")
        return

    

    sql_query = """
    INSERT INTO users(name,email,gender,password)
    VALUES
    (%s,%s,%s,%s);
    """


    cursor.execute(sql_query,(name,email,gender,password))
    user_id = cursor.fetchone()[0]
    db.commit()
    print("\n ✔ Signup Completed!")
    print("*" * 50)
           
    session.set_user({
        "id": user_id,
        "name": name,
        "email": email,
    })

    user_menu()

    



