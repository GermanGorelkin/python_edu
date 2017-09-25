from . import db
from sqlalchemy import insert


def init_insert():
    ins = db.cookies.insert().values(
        cookie_name="chocolate chip",
        cookie_recipe_url="http://some.aweso.me/cookie/recipe.html",
        cookie_sku="CC01",
        quantity="12",
        unit_cost="0.50"
    )

    result = db.engine.execute(ins)
    print(result.inserted_primary_key)

    ins = insert(db.cookies).values(
        cookie_name="chocolate chip",
        cookie_recipe_url="http://some.aweso.me/cookie/recipe.html",
        cookie_sku="CC01",
        quantity="12",
        unit_cost="0.50"
    )

    result = db.engine.execute(ins)
    print(result.inserted_primary_key)

    ins = db.cookies.insert()
    result = db.engine.execute(
        ins,
        cookie_name="chocolate chip",
        cookie_recipe_url="http://some.aweso.me/cookie/recipe.html",
        cookie_sku="CC01",
        quantity="12",
        unit_cost="0.50"
    )

    result = db.engine.execute(ins)
    print(result.inserted_primary_key)

    inventory_list = [
        {
            'cookie_name': 'peanut butter',
            'cookie_recipe_url': 'http://some.aweso.me/cookie/peanut.html',
            'cookie_sku': 'PB01',
            'quantity': '24',
            'unit_cost': '0.25'
        },
        {
            'cookie_name': 'oatmeal raisin',
            'cookie_recipe_url': 'http://some.okay.me/cookie/raisin.html',
            'cookie_sku': 'EWW01',
            'quantity': '100',
            'unit_cost': '1.00'
        }
    ]
    result = db.engine.execute(ins, inventory_list)

if __name__ == '__main__':
    init_insert()
