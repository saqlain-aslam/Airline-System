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
        departure_time = str(input("\n Enter departure time in proper format(YYYY-MM-DD 00:00:00):"))
        arrival_time = str(input("\n Enter arrival time in proper format(YYYY-MM-DD 00:00:00):"))
        plane_id = str(input("\n Enter plane id:"))

        # plane available
        available_plane = """
        SELECT plane_id, departure_time
        FROM routes
        WHERE  departure_time = %s and plane_id = %s;
        """
        cursor.execute(available_plane,(departure_time,plane_id))
        plane_available = cursor.fetchone()

        if(plane_available):
          print(f"\n  🚨 Plane with {plane_id} is already booked at this time! Kindly select another Plane.")
          return


        sql_query = """
        INSERT INTO routes(route_id, origin, destination, departure_time, arrival_time, plane_id)
        VALUES
        (%s,%s,%s,%s,%s,%s);
        """


        cursor.execute(sql_query,(route_id,origin,destination,departure_time,arrival_time,plane_id))
        db.commit()
        print("\n ✔ New Route Added!")
        print("*" * 50)
           

    except Exception as e:
        print("⚠️ Unexpected Error:", e)
    



