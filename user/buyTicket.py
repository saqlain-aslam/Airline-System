from database.connection import DatabaseConnection

def BuyTicket():

    db = DatabaseConnection()
    db.connect()
    cursor = db.get_cursor()
    
    print("*" * 50 )
    print("\n 💻 Kindly enter Following data to buy ticket! \n")
    print("*" * 50)

    user_ID = int(input("\n Enter your User ID:"))

    # seat_number check
    seat_number = int(input("\n Enter seat number:"))
    if(seat_number > 40 or seat_number <= 0):
        print("\n 🚨 Kindly enter seat number between 1 and 40.")
        return
    else:
        pass

    flight_id = str(input("\n Enter your selected Flight ID:"))

    if not flight_id:
        print("\n 🚨 Kindly enter Flight ID.")
        return
    else:
        pass

    # check seat availability
    available_query = """
    SELECT seat_number
    FROM ticket
    WHERE  seat_number = %s and route_id = %s;
    """
    cursor.execute(available_query,(seat_number,flight_id))
    seat_available = cursor.fetchone()

    if(seat_available):
        print(f"\n  🚨 Seat number {seat_number} in flight {flight_id} is already booked by someone! Kindly select another seat.")
        return
     
    
    luggage_weight = float(input("\n Enter your luggage weight:"))
    gender = input("\n Enter your gender(Male/Female):").strip().capitalize()

    
    # gender check

    if (seat_number % 2 == 0):
        fetch_gender = seat_number - 1
    else:
        fetch_gender = seat_number + 1

    gender_query = """
    SELECT gender
    FROM ticket
    WHERE  seat_number = %s AND route_id = %s;
    """

    cursor.execute(gender_query,(fetch_gender,flight_id))   
    result = cursor.fetchone()

    if result:
        partner_gender = result[0]
        if partner_gender != gender:
            print("🚨 You cannot have seat pair to opposite gender!Kindly select some other seat.")
            return
    else:
        pass


    # get plane id
    planid_query = """  
    SELECT plane_id FROM routes
    WHERE route_id = %s;
    """
    
    cursor.execute(planid_query,(flight_id,)) 
    plane_id = cursor.fetchone()[0]

    # print(plane_id)

    ticket_query = """
    INSERT INTO ticket(user_id, route_id, plane_id, seat_number, luggage_weight, gender)
    VALUES
    (%s,%s,%s,%s,%s,%s);
    """

    time_valid = """
    SELECT departure_time
    FROM routes
    WHERE route_id = %s and now() < departure_time;
    """
    cursor.execute(time_valid,(flight_id,))
    departure_time = cursor.fetchone()

    # print(f"DEPARTUTRE: {departure_time}")


    if(departure_time):
        if( user_ID and seat_number and gender and luggage_weight and plane_id):
           cursor.execute(ticket_query,(user_ID,flight_id,plane_id,seat_number,luggage_weight,gender))
           db.commit()
           print("\n ✔ Ticket Booked")
           print("*" * 50)
        else:
            print("\n ❌ Ticket not booked!")
    else:
        print("\n ❌ Your selected flight have departed. Kindly Select the Flight from Future")
