from pony.orm import db_session
import entities


@db_session
def test_create_category():
    test_name = 'TEST'
    entities.DBConnection.db.bind(provider='sqlite', filename=':memory:')

    cat1 = entities.Category(name=test_name)

    assert cat1.name == test_name
