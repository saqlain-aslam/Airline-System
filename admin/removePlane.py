from database.connection import DatabaseConnection

def RemovePlane():
    try:

        db = DatabaseConnection()
        db.connect()
  
        cursor = db.get_cursor()
    
        print("*" * 50 )
        print("\n 💻 Enter data to remove Plane! \n")
        print("*" * 50)

        plane_id = str(input("\n Enter your Plane ID:"))
        name = str(input("\n Enter your plane name:"))
        model = str(input("\n Enter your plane model:"))


        sql_query = """
        DELETE FROM plane
        WHERE
        plane_id = %s AND name = %s AND model = %s;
        """


        if( plane_id and name and model):
            cursor.execute(sql_query,(plane_id,name,model))
            db.commit()
            print(f"\n ✔ Plane with {plane_id} ID removed!")
            print("*" * 50)
           
        else:
            print("❌ Kindly enter complete data")
   
    except Exception as e:
        print("⚠️ Unexpected Error:", e)

    



