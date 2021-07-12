from pony.orm import db_session
from pony.converting import str2datetime

import os
import sys

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

import entities


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
        amount=100,
    )

    assert bank_entry.ingCategory != 1
