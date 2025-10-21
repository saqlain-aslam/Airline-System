from database.connection import DatabaseConnection

def ChangePassword():

    db = DatabaseConnection()
    db.connect()
  
    cursor = db.get_cursor()
    
    print("*" * 50 )
    
    print("\n 💻 Kindly enter your email and new password! \n")
    print("*" * 50)

    email = str(input("\n Enter your email:"))
    password = str(input("\n Enter your new password:"))

    passsword_query = """
    UPDATE users
    SET password = %s
    WHERE email = %s;1
    
    """
    
    password_change = cursor.execute(passsword_query, (password,email))
    db.commit()

    # print(f"passwor change: {password_change}")

    if cursor.rowcount > 0:
      print("*" * 50)
      print("✔ Password changed successfully!")
      print("*" * 50)
    else:
      print("❌ Password could not change. Check again.")    


