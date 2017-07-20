import db
import insert
from sqlalchemy.sql import select


def querying_data():
    print('-' * 10)
    s = select([db.cookies])
    rp = db.engine.execute(s)
    for row in rp:
        print(row)

    print('-' * 10)
    s = db.cookies.select()
    rp = db.engine.execute(s)
    results = rp.fetchall()
    for row in results:
        print(row)

    print('-' * 10)
    first_row = results[0]
    print(first_row)
    print(first_row[1])
    print(first_row.cookie_name)
    print(first_row[db.cookies.c.cookie_name])


if __name__ == '__main__':
    insert.init_insert()
    querying_data()
