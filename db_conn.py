from dataclasses import dataclass
import conf_management as conf
from pony.orm import Database


@dataclass
class DBConnection:
    db_user: str = conf.get_db_user()
    db_pass: str = conf.get_db_pass()
    db_host: str = conf.get_db_host()
    db_database: str = conf.get_db_database()
    db_provider: str = conf.get_db_provider()

    db = Database()
    db.bind(provider=db_provider, user=db_user, password=db_pass, host=db_host,
            database=db_database)
