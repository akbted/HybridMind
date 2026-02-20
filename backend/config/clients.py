from backend.config.setting import proj_settings, db_settings
from psycopg2 import pool
import threading

# DB_CLIENT
class DBClient:
    def __init__(self, db_settings):
        self.connection_pool = db_settings.connection_pool
    
    def get_connection(self):
        return self.connection_pool.getconn()

    def release_connection(self, conn):
        return self.connection_pool.putconn(conn)

db_client = DBClient(db_settings)
conn = db_client.get_connection()
db_client.release_connection(conn)
