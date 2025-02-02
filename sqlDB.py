import mysql.connector
from dotenv import load_dotenv
import os

class DatabaseConnection:

    def __init__(self):

        load_dotenv()
        self.host = os.getenv('DB_HOST')
        self.user = os.getenv('DB_USER')
        self.password = os.getenv('DB_PASSWORD')
        self.port = int(os.getenv('DB_PORT', 3306))
        self.database = os.getenv('DB_DATABASE')

        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                port=self.port,
                database=self.database
            )
            print("Database connection established successfully!")
        except mysql.connector.Error as err:
            print("Connection error:", err)




    def close(self):
        if self.connection:
            self.connection.close()
            print("Database connection closed.")

    def findOne(self, query):

        if not self.connection:
            print("Error: Database connection not established.")
            return None

        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            result = cursor.fetchone()
            return result

        except mysql.connector.Error as err:
            print("Error executing query:", err)
            return None

    def fetch_all(self, query):

        if not self.connection:
            print("Error: Database connection not established.")
            return None

        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
            return result

        except mysql.connector.Error as err:
            print("Error executing query:", err)
            return None
