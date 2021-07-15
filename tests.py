import myconstants
from prettytable import PrettyTable

myconstants.POSTGRE_PROVIDER = None


from pony.orm import db_session
from pony.converting import str2datetime
import entities
import main


@db_session
def test_create_ingcategory():
    test_name = "TEST"

    cat1 = entities.IngCategory(name=test_name)

    assert cat1.name == test_name


@db_session
def test_create_ingsubcategory():
    test_name = "TEST"

    cat1 = entities.IngSubcategory(name=test_name)

    assert cat1.name == test_name


@db_session
def test_create_owncategory():
    test_name = "TEST"

    cat1 = entities.OwnCategory(name=test_name)

    assert cat1.name == test_name


@db_session
def test_create_ownsubcategory():
    test_name = "TEST"

    cat1 = entities.OwnSubcategory(name=test_name)

    assert cat1.name == test_name


@db_session
def test_create_bank_entry():
    bank_entry = entities.BankEntry(
        entryDate=str2datetime("2012-10-20 15:22:00"),
        ingCategory=1,
        ingSubcategory=1,
        ownCategory=1,
        ownSubcategory=1,
        amount=100,
    )

    assert bank_entry.ingCategory != 1


@db_session
def test_pretty_table_menu():
    entities.BankEntry(
        entryDate=str2datetime("2012-10-20 15:22:00"),
        ingCategory=1,
        ingSubcategory=1,
        amount=-43.2,
        description="Pago en COMPRA ZAPATO FEROZ",
    )

    entities.BankEntry(
        entryDate=str2datetime("2012-10-20 15:22:00"),
        ingCategory=1,
        ingSubcategory=1,
        amount=-220.74,
        description="Recibo LA UNION ALCOYANA S.A.",
    )

    entries = main.get_pending_entries()

    x = PrettyTable()

    x.field_names = main.get_colnames()

    rows = [main.get_row(entry) for entry in entries]

    x.add_rows(rows)

    result = """+----+------------+-----------------+-------------------+--------------------+----------------------+-----------------+--------------------+---------+-------------------------------+--------------+
| Id | Entry date | ING Category Id | ING Category Name | ING Subcategory Id | ING Subcategory Name | Own Category Id | Own Subcategory Id |  Amount |          Description          | Expense Type |
+----+------------+-----------------+-------------------+--------------------+----------------------+-----------------+--------------------+---------+-------------------------------+--------------+
| 2  | 2012-10-20 |        1        |        TEST       |         1          |         TEST         |       None      |        None        |  -43.2  |  Pago en COMPRA ZAPATO FEROZ  |     None     |
| 3  | 2012-10-20 |        1        |        TEST       |         1          |         TEST         |       None      |        None        | -220.74 | Recibo LA UNION ALCOYANA S.A. |     None     |
+----+------------+-----------------+-------------------+--------------------+----------------------+-----------------+--------------------+---------+-------------------------------+--------------+"""

    assert str(x) == result
