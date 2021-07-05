import category
from pony.orm import db_session


@db_session
def create_test_category():
    cat1 = category.Category(name='YEAHHH', ing=True)

    print(cat1.name)


if __name__ == '__main__':
    create_test_category()
