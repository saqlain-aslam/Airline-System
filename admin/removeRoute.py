from database.connection import DatabaseConnection

def RemoveRoute():
    try:

        db = DatabaseConnection()
        db.connect()
  
        cursor = db.get_cursor()
    
        print("*" * 50 )
        print("\n 💻 Enter data to remove Route! \n")
        print("*" * 50)

        route_id = str(input("\n Enter Route ID:"))

        if(route_id):
            pass
        else:
            print("❌ Kindly enter complete data")

        sql_query = """
        DELETE FROM routes
        WHERE
        route_id = %s;
        """
        cursor.execute(sql_query,(route_id,))
        db.commit()
        
        if cursor.rowcount > 0:
            print(f"\n ✔ Route {route_id} removed!")
            print("*" * 50)
        else:
            print("🚨 Kindly enter correct ID")    
            return
    except Exception as e:
        print("⚠️ Unexpected Error:", e)
    



