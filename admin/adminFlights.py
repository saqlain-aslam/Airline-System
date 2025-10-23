from database.connection import DatabaseConnection

def AdminFlights():
    try:

        db = DatabaseConnection()
        db.connect()
  
        cursor = db.get_cursor()
    
        print("*" * 50 )
    
        print("\n ✈ Following are the All schedule Flights! \n")
        print("*" * 50)

        flight_query = """
        SELECT * FROM routes;
        """
    
        cursor.execute(flight_query)
        flights = cursor.fetchall()

        if cursor.rowcount > 0:
            print("✈✈✈✈    Available Flights:    ✈✈✈✈")
        
            for flight in flights:
                print("\n" + "✈️  FLIGHT INFORMATION".center(60, "="))
                print(f"""
                | Flight ID        : {flight[0]}
                | Origin           : {flight[1]}
                | Destination      : {flight[2]}
                | Departure Time   : {flight[3]}
                | Arrival Time     : {flight[4]}
                | Plane Assigned   : {flight[5]}
                """)
                print("=" * 60)
        else:
            print("😢 Sorry currently we don't have avalable flights for you!")
    except Exception as e:
        print("⚠️ Unexpected Error:", e)


