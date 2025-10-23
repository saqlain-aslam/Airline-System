from database.connection import DatabaseConnection


def Users():
    try:

        db = DatabaseConnection()
        db.connect()
  
        cursor = db.get_cursor()
    
        print("*" * 50 )
    
        print("\n ✈ Following are the Planes! \n")
        print("*" * 50)

        plane_query = """
        SELECT * FROM users;
        """
 
        cursor.execute(plane_query)
        users = cursor.fetchall()

        if cursor.rowcount > 0:
            print("     🤵🤵🤵🤵    Registered Users:    🤵🤵🤵🤵")
        
            for user in users:
                print("\n" + "🤵  Plane INFORMATION".center(60, "="))
                print(f"""
                | Name            : {user[1]}
                | Email           : {user[2]}
                | Gender          : {user[3]}
                """)
                print("=" * 60)
        else:
            print("😢 No one registered")
    except Exception as e:
        print("⚠️ Unexpected Error:", e)


