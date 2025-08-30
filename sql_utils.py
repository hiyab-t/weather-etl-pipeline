import os
import psycopg2 as psycopg
from dotenv import load_dotenv

load_dotenv(
)
host_name = os.environ.get("POSTGRES_HOST")
database_name = os.environ.get("POSTGRES_DB")
user_name = os.environ.get("POSTGRES_USER")
user_password = os.environ.get("POSTGRES_PASSWORD")

config = f"""
        host={host_name}
        dbname={database_name}
        user={user_name}
        password={user_password}"""

