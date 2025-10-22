from database.connection import DatabaseConnection

def TicketCancel():

    db = DatabaseConnection()
    db.connect()
    cursor = db.get_cursor()
    
    print("*" * 50 )
    print("\n 💻 Cancel your Booed Ticket! \n")
    print("*" * 50)

    ticket_id = input("Enter your Ticket ID: ")
    
    if not ticket_id:
        print("🚨 Kindly enter the Ticket ID:")
        return


    cancel_query = """
    DELETE FROM ticket
    WHERE ticket_id = %s;
    """

    cursor.execute(cancel_query, (ticket_id,))
    db.commit()

    if cursor.rowcount > 0:
        print("*" * 50)
        print("✔ Ticket Cancelled")
        print("*" * 50)
    else:
        print("*" * 50)
        print("❌ Failed to cancel Ticket!")
        print("*" * 50)
    
    
