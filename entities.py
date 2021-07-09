from db_conn import DBConnection
from pony.orm import PrimaryKey, Required, Optional, Set
from datetime import date

my_conn = DBConnection()


class IngCategory(my_conn.db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Required(str, unique=True)
    bank_entries = Set("BankEntry", reverse="ingCategory")


class IngSubcategory(my_conn.db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Required(str, unique=True)
    bank_entries = Set("BankEntry", reverse="ingSubcategory")


class OwnCategory(my_conn.db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Required(str, unique=True)
    bank_entries = Set("BankEntry", reverse="ownCategory")


class OwnSubcategory(my_conn.db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Required(str, unique=True)
    bank_entries = Set("BankEntry", reverse="ownSubcategory")


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
    entryDate = Required(date)
    ingCategory = Optional(IngCategory, reverse="bank_entries")
    ingSubcategory = Optional(IngSubcategory, reverse="bank_entries")
    ownCategory = Optional(OwnCategory, reverse="bank_entries")
    ownSubcategory = Optional(OwnSubcategory, reverse="bank_entries")
    amount = Required(float)
    balance = Optional(float)
    description = Optional(str)


my_conn.db.generate_mapping(create_tables=True)
