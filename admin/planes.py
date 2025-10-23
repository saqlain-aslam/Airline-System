from database.connection import DatabaseConnection


def Planes():
    try:

        db = DatabaseConnection()
        db.connect()
  
        cursor = db.get_cursor()
    
        print("*" * 50 )
    
        print("\n ✈ Following are the Planes! \n")
        print("*" * 50)

        plane_query = """
        SELECT * FROM plane;
        """
        
 
        cursor.execute(plane_query)
        planes = cursor.fetchall()

        if cursor.rowcount > 0:
            print("✈✈✈✈    Available Planes:    ✈✈✈✈")
        
            for plane in planes:
                print("\n" + "✈️  Plane INFORMATION".center(60, "="))
                print(f"""
                | Plane ID       : {plane[0]}
                | Name           : {plane[1]}
                | Model          : {plane[2]}
                """)
                print("=" * 60)
        else:
            print("😢 Sorry currently we don't have avalable planes for you!")
    except Exception as e:
        print("⚠️ Unexpected Error:", e)


