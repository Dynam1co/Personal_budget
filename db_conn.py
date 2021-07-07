from dataclasses import dataclass
from pony.orm import Database
import myconstants


@dataclass
class DBConnection:
    db_user: str = myconstants.POSTGRE_USER
    db_pass: str = myconstants.POSTGRE_PASS
    db_host: str = myconstants.POSTGRE_HOST
    db_database: str = myconstants.POSTGRE_DATABASE
    db_provider: str = myconstants.POSTGRE_PROVIDER

    db = Database()

    if db_provider:
        db.bind(
            provider=db_provider,
            user=db_user,
            password=db_pass,
            host=db_host,
            database=db_database,
        )
    else:  # In test use in memory database
        db.bind(provider="sqlite", filename=":memory:")
