from database.connection import DatabaseConnection

def Flights():

    db = DatabaseConnection()
    db.connect()
  
    cursor = db.get_cursor()
    
    print("*" * 50 )
    
    print("\n ✈ Following are the schedule Flights! \n")
    print("*" * 50)

    flight_query = """
    SELECT * FROM routes;
    """
    
    cursor.execute(flight_query)
    flights = cursor.fetchall()

    for flight in flights:
        print(f"🛫 Flight ID: {flight[0]}, 🌍 Origin: {flight[1]}, 🌟 Destination: {flight[2]}, ⌚ Departure Time: {flight[3]}, ⏲ Arrival Time: {flight[4]}, ✈ Plane: {flight[5]} \n")
        


