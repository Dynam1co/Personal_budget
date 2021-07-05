from dataclasses import dataclass
from pony.orm import Database
import os
from dotenv import load_dotenv

load_dotenv()


@dataclass
class DBConnection:
    db_user: str = os.getenv('POSTGRE_USER')
    db_pass: str = os.getenv('POSTGRE_PASS')
    db_host: str = os.getenv('POSTGRE_HOST')
    db_database: str = os.getenv('POSTGRE_DATABASE')
    db_provider: str = os.getenv('POSTGRE_PROVIDER')

    db = Database()
    db.bind(provider=db_provider, user=db_user, password=db_pass, host=db_host,
            database=db_database)
