"""Used to categorize entries automatically"""

from pony.orm.core import select
import entities
from pony.orm import db_session


def categorize_new_entries():
    # Get maping rules
    rules = get_map_table()

    # Apply rules to categorize pending entries
    for rule in rules:
        get_entry_by_rules_and_apply_category(rule)


@db_session
def get_map_table():
    return select(r for r in entities.MappingCategories)[:]


@db_session
def get_entry_by_rules_and_apply_category(rule):
    # Get entries pending categorization
    pending_entries = get_entries_to_categorize(rule)

    # Apply category and subcategory for each entry
    for entry in pending_entries:
        apply_category_to_entry(entry, rule.catId, rule.subcatId)


@db_session
def apply_category_to_entry(entry, category, subcategory):
    entry.ownCategory = category.id
    entry.ownSubcategory = subcategory.id


@db_session
def get_entries_to_categorize(rule):
    query = get_query_to_select_entries(rule)

    return entities.BankEntry.select_by_sql(query)[:]


def get_query_to_select_entries(rule):
    query = f"""SELECT * FROM bankentry WHERE
        owncategory IS NULL
        AND LOWER(description) LIKE '%{rule.textToFind.lower()}%'"""

    if rule.textoToExclude != "":
        query += f" AND LOWER(description) NOT LIKE '%{rule.textoToExclude.lower()}%'"

    return query
