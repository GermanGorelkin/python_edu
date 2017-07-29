from .db import engine, cookies
from . import insert
from sqlalchemy.sql import select, desc, func, and_, or_, not_


def querying_data():
    print('-' * 10)
    s = select([cookies])
    rp = engine.execute(s)
    for row in rp:
        print(row)

    print('-' * 10)
    s = cookies.select()
    rp = engine.execute(s)
    results = rp.fetchall()
    for row in results:
        print(row)

    print('-' * 10)
    first_row = results[0]
    print(first_row)
    print(first_row[1])
    print(first_row.cookie_name)
    print(first_row[cookies.c.cookie_name])


def ordering():
    print('-' * 10)
    # ORDER BY
    s = select([cookies.c.cookie_name, cookies.c.quantity])
    s = s.order_by(cookies.c.quantity)
    rp = engine.execute(s)
    for cookie in rp:
        print('{} - {}'.format(cookie.quantity, cookie.cookie_name))

    print('-' * 10)
    # ORDER BY DESC
    s = select([cookies.c.cookie_name, cookies.c.quantity])
    s = s.order_by(desc(cookies.c.quantity))
    rp = engine.execute(s)
    for cookie in rp:
        print('{} - {}'.format(cookie.quantity, cookie.cookie_name))


def limiting():
    print('-' * 10)
    # LIMIT 2 OFFSET 0
    s = select([cookies.c.cookie_name, cookies.c.quantity])
    s = s.order_by(cookies.c.quantity)
    s = s.limit(2)
    rp = engine.execute(s)
    print([result.cookie_name for result in rp])


def sql_functions():
    print('-' * 10)
    # SUM()
    s = select([func.sum(cookies.c.quantity)])
    rp = engine.execute(s)
    print(rp.scalar())

    print('-' * 10)
    # COUNT()
    s = select([func.count(cookies.c.cookie_name)])
    rp = engine.execute(s)
    record = rp.first()
    print(record.keys())
    print(record.count_1)

    print('-' * 10)
    # COUNT() as
    s = select([func.count(cookies.c.cookie_name).label('inventory_count')])
    rp = engine.execute(s)
    record = rp.first()
    print(record.keys())
    print(record.inventory_count)


def filtering():
    print('-' * 10)
    # WHERE name = ''
    s = select([cookies]).where(cookies.c.cookie_name == 'chocolate chip')
    rp = engine.execute(s)
    record = rp.first()
    print(record.items())

    print('-' * 10)
    # LIKE '%%'
    s = select([cookies]).where(cookies.c.cookie_name.like('%chocolate%'))
    rp = engine.execute(s)
    for record in rp.fetchall():
        print(record.cookie_name)


def conjunctions():
    print('-' * 10)
    # quantity > 23 AND cookies.unit_cost < 0.40
    s = select([cookies]).where(
        and_(
            cookies.c.quantity > 23,
            cookies.c.unit_cost < 0.40
        )
    )
    for row in engine.execute(s):
        print(row.cookie_name)

    print('-' * 10)
    #  BETWEEN 10 AND 50 OR (cookie_name LIKE '%chip%')
    s = select([cookies]).where(
        or_(
            cookies.c.quantity.between(10, 50),
            cookies.c.cookie_name.contains('chip')
        )
    )
    for row in engine.execute(s):
        print(row.cookie_name)


def select_data():
    querying_data()
    ordering()
    limiting()
    sql_functions()
    filtering()
    conjunctions()


if __name__ == '__main__':
    insert.init_insert()
    select_data()
