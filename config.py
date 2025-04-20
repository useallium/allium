from dotenv import load_dotenv
import os

load_dotenv()

MYSQL_CONFIG = {
    'host':os.getenv("HOST"),
    'user':os.getenv("USER"),
    'password':os.getenv("PASSWORD"),
    'database':os.getenv("DATABASE"),
}