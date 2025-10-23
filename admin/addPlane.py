from database.connection import DatabaseConnection

def AddPlane():
    try:

        db = DatabaseConnection()
        db.connect()
  
        cursor = db.get_cursor()
    
        print("*" * 50 )
    
        print("\n 💻 Enter data to add new Plane! \n")
        print("*" * 50)

        plane_id = str(input("\n Enter your Plane ID:"))
        name = str(input("\n Enter your plane name:"))
        model = str(input("\n Enter your plane model:"))
        total_seats = 40


        sql_query = """
        INSERT INTO plane(plane_id, name, model, total_seats)
        VALUES
        (%s,%s,%s,%s);
        """


        if( plane_id and name and model):
           cursor.execute(sql_query,(plane_id,name,model,total_seats))
           db.commit()
           print("\n ✔ New Plane Added!")
           print("*" * 50)
           
        else:
            print("❌ Kindly enter complete data")
   
    except Exception as e:
        print("⚠️ Unexpected Error:", e)
    



