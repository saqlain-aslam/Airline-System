from database.connection import DatabaseConnection

def MyTicket():

    db = DatabaseConnection()
    db.connect()
    cursor = db.get_cursor()
    
    print("*" * 50 )
    print("\n 💻 My Booked Tickets! \n")
    print("*" * 50)

    user_id = input("Enter your User ID: ")

    myticket_query = """
    SELECT t.ticket_id, u.name AS passenger, r.origin, r.destination, p.name AS plane_name, r.departure_time, r.arrival_time, t.seat_number
    FROM ticket t
    JOIN users u ON t.user_id = u.id
    JOIN routes r ON t.route_id = r.route_id
    JOIN plane p ON t.plane_id = p.plane_id
    WHERE t.user_id = %s;
    """

    cursor.execute(myticket_query, (user_id,))
    records = cursor.fetchall()

    for row in records:
        print(f"\nTicket ID: {row[0]}")
        print(f"Passenger: {row[1]}")
        print(f"Seat number: {row[7]}")
        print(f"Route: {row[2]} → {row[3]}")
        print(f"Plane: {row[4]}")
        print(f"Departure: {row[5]}")
        print(f"Arrival: {row[6]}")
