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
    subcategories = Set("OwnSubcategory", reverse="main_category")
    mapCats = Set("MappingCategories", reverse="catId")


class OwnSubcategory(my_conn.db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Required(str)
    bank_entries = Set("BankEntry", reverse="ownSubcategory")
    main_category = Optional(OwnCategory, reverse="subcategories")
    mapSubCats = Set("MappingCategories", reverse="subcatId")


class MappingCategories(my_conn.db.Entity):
    id = PrimaryKey(int, auto=True)
    textToFind = Required(str)
    textoToExclude = Optional(str)
    catId = Required(OwnCategory, reverse="mapCats")
    subcatId = Required(OwnSubcategory, reverse="mapSubCats")


class ExpenseType(my_conn.db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Required(str)
    periodicity = Required(str)
    bank_entries = Set("BankEntry", reverse="expenseType")


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
    expenseType = Optional(ExpenseType, reverse="bank_entries")


my_conn.db.generate_mapping(create_tables=True)
