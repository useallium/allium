from mysql.connector import pooling
from dotenv import load_dotenv
import os

load_dotenv()

db_config = {
    'host':os.getenv("HOST"),
    'user':os.getenv("USER"),
    'password':os.getenv("PASSWORD"),
    'database':os.getenv("DATABASE"),
    'port':int(os.getenv("PORT"))
}

connection_pool = pooling.MySQLConnectionPool(
    pool_name="allium_pool",
    pool_size=5,
    **db_config
)

def connect():
    return connection_pool.get_connection()


class Database:
    def __init__(self):
        self.conn = connect()
        self.cursor = self.conn.cursor(dictionary=True)

    def close(self):
        self.cursor.close()
        self.conn.close()
