from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

load_dotenv()

# Oracle 접속 정보
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_SERVICE = os.getenv("DB_SERVICE")
DATABASE_URL = (
    f"oracle+oracledb://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/?service_name={DB_SERVICE}"
)
 
engine = create_engine(
    DATABASE_URL,
    echo=True
)