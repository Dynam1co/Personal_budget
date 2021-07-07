import os
from dotenv import load_dotenv

load_dotenv()

# Excel paths
PROCESS_PATH = os.getenv("PROCESS_PATH")
PROCESSED_PATH = os.getenv("PROCESSED_PATH")

# Initial excel row to import
INITIAL_ROW = int(os.getenv("INITIAL_ROW"))

# PostgreSQL
POSTGRE_USER = os.getenv("POSTGRE_USER")
POSTGRE_PASS = os.getenv("POSTGRE_PASS")
POSTGRE_HOST = os.getenv("POSTGRE_HOST")
POSTGRE_DATABASE = os.getenv("POSTGRE_DATABASE")
POSTGRE_PROVIDER = os.getenv("POSTGRE_PROVIDER")
