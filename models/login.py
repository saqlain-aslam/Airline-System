from database.connection import DatabaseConnection

def Login():

    db = DatabaseConnection()
    db.connect()
  
    cursor = db.get_cursor()
    
    print("*" * 50 )
    print("\n 💻 Enter your email and password to Login! \n")
    print("*" * 50)


    email = str(input("\n Enter your email:"))
    password = str(input("\n Enter your password:"))

    sql_query = """
    SELECT email FROM users WHERE email = %s AND password = %s;
    """
    
   
    cursor.execute(sql_query,(email, password))
    test_user = cursor.fetchall()
     

    if( test_user):
        print("\n ✔ Login Successfully!")
        print("*" * 50)

    else:
       print("❌ Kindly enter valid credentials and If you don't have account Signup first!")



