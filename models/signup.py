from database.connection import DatabaseConnection
from utils.usermenu import user_menu

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

    email_query = """
    SELECT email FROM users WHERE email = %s;
    """

    cursor.execute(email_query, (email,))
    test_email = cursor.fetchall()


    sql_query = """
    INSERT INTO users(name,email,gender,password)
    VALUES
    (%s,%s,%s,%s);
    """


    if (not test_email):
        if( name and email and gender and password):
           cursor.execute(sql_query,(name,email,gender,password))
           db.commit()
           print("\n ✔ Signup Completed!")
           print("*" * 50)
           user_menu()
        else:
            print("❌ Kindly enter complete data")
    else:
        print("\n ❌ Email already exists. Please go for Login!")




