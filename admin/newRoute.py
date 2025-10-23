from database.connection import DatabaseConnection

def AddRoute():
    try:

        db = DatabaseConnection()
        db.connect()
  
        cursor = db.get_cursor()
    
        print("*" * 50 )
    
        print("\n 💻 Enter data to add new Route! \n")
        print("*" * 50)

        route_id = str(input("\n Enter route ID:"))
        origin = str(input("\n Enter origin:"))
        destination = str(input("\n Enter destination:"))
        departure_time = str(input("\n Enter departure time:"))
        arrival_time = str(input("\n Enter arrival time:"))
        plane_id = str(input("\n Enter plane id:"))


        sql_query = """
        INSERT INTO routes(route_id, origin, destination, departure_time, arrival_time, plane_id)
        VALUES
        (%s,%s,%s,%s,%s,%s);
        """


        if( route_id and origin and destination and departure_time and arrival_time and plane_id):
           cursor.execute(sql_query,(route_id,origin,destination,departure_time,arrival_time,plane_id))
           db.commit()
           print("\n ✔ New Route Added!")
           print("*" * 50)
           
        else:
            print("❌ Kindly enter complete data")

    except Exception as e:
        print("⚠️ Unexpected Error:", e)
    



