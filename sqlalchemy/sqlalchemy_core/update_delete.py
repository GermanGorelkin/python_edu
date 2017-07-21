from db import engine, cookies
import insert
from sqlalchemy.sql import select, update, delete


def update_data():
    print('-' * 10)
    # SET quantity = quantity + 120 WHERE cookie_name == 'chocolate chip'
    u = update(cookies).where(cookies.c.cookie_name == "chocolate chip")
    u = u.values(quantity=(cookies.c.quantity + 120))
    result = engine.execute(u)
    print(result.rowcount)  # кол-во измененных строк
    s = select([cookies]).where(cookies.c.cookie_name == "chocolate chip")
    result = engine.execute(s).first()
    for key in result.keys():
        print('{:>20}: {}'.format(key, result[key]))


def delete_data():
    u = delete(cookies).where(cookies.c.cookie_name == "dark chocolate chip")
    result = engine.execute(u)
    print(result.rowcount)
    s = select([cookies]).where(cookies.c.cookie_name == "dark chocolate chip")
    result = engine.execute(s).fetchall()
    print(len(result))


if __name__ == '__main__':
    insert.init_insert()
    update_data()
    delete_data()
