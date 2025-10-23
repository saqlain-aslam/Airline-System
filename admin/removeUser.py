from database.connection import DatabaseConnection

def RemoveUser():
    try:     

        db = DatabaseConnection()
        db.connect()
  
        cursor = db.get_cursor()
    
        print("*" * 50 )
        print("\n 💻 Enter data to remove User! \n")
        print("*" * 50)

        name = str(input("\n Enter user name:"))
        email = str(input("\n Enter user email:"))


        sql_query = """
        DELETE FROM users
        WHERE
        name = %s AND email = %s;
        """

        if(name and email):
           cursor.execute(sql_query,(name,email))
           db.commit()
           print(f"\n ✔ {name} removed!")
           print("*" * 50)
           
        else:
            print("❌ Kindly enter complete data")
   
    except Exception as e:
        print("⚠️ Unexpected Error:", e)
    



