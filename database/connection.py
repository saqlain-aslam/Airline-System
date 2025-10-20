import psycopg2
import os
from dotenv import load_dotenv

class DatabaseConnection:
    def __init__(self):

        load_dotenv()

        self.host = os.getenv("DB_HOST")
        self.dbname = os.getenv("DB_NAME")
        self.user = os.getenv("DB_USER")
        self.password = os.getenv("DB_PASS")
        self.port = os.getenv("DB_PORT")
        self.connection = None

    def connect(self):
        try:
            self.connection = psycopg2.connect(
                host=self.host,
                dbname=self.dbname,
                user=self.user,
                password=self.password,
                port=self.port
            )
            print(" Database connected successfully!") 
            # print(os.getcwd()) 
        except Exception as e:
            print(" Error connecting to database:", e)

    def get_cursor(self):
        if self.connection:
            return self.connection.cursor()
            # cursor = self.connection.cursor()
            # cursor.execute("SELECT * FROM users")
            # rows = cursor.fetchall()
            # for row in rows:
            #     print(row)
            # return cursor
            
        else:
            print("No active database connection.")
            return None

    def commit(self):
        if self.connection:
            self.connection.commit()

    def close(self):
        if self.connection:
            self.connection.close()
            print(" Database connection closed.")
