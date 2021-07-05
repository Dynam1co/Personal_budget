from db_conn import DBConnection
from pony.orm import PrimaryKey, Required, Optional
from datetime import datetime

my_conn = DBConnection()


class Category(my_conn.db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Required(str, unique=True)
    ing = Optional(bool)


class Subcategory(my_conn.db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Required(str, unique=True)
    ing = Optional(bool)


class MappingCategory(my_conn.db.Entity):
    ingId = Required(int)
    ownId = Required(int)

    PrimaryKey(ingId, ownId)


class MappingSubCategory(my_conn.db.Entity):
    ingId = Required(int)
    ownId = Required(int)

    PrimaryKey(ingId, ownId)


class BankEntry(my_conn.db.Entity):
    id = PrimaryKey(int, auto=True)
    entryDate: Required(datetime)
    ingCategory: Optional(Category)
    ingSubcategory: Optional(Subcategory)
    ownCategory: Optional(Category)
    ownSubcategory: Optional(Subcategory)
    amount: Required(float)
    balance: Optional(float)


my_conn.db.generate_mapping(create_tables=True)
