from db_conn import DBConnection
from pony.orm import PrimaryKey, Required, Optional

my_conn = DBConnection()


class Category(my_conn.db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Required(str, unique=True)
    ing = Optional(bool)


my_conn.db.generate_mapping(create_tables=True)
