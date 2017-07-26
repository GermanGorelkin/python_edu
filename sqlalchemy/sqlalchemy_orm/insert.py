import db


def init_insert():
    # commit
    cc_cookie = db.Cookie(cookie_name='chocolate chip',
                          cookie_recipe_url='http://some.aweso.me/cookie/recipe.html',
                          cookie_sku='CC01',
                          quantity=12,
                          unit_cost=0.50)
    db.session.add(cc_cookie)
    db.session.commit()
    print(cc_cookie.cookie_id)

    # flush
    dcc = db.Cookie(cookie_name='dark chocolate chip',
                    cookie_recipe_url='http://some.aweso.me/cookie/recipe_dark.html',
                    cookie_sku='CC02',
                    quantity=1,
                    unit_cost=0.75)
    mol = db.Cookie(cookie_name='molasses',
                    cookie_recipe_url='http://some.aweso.me/cookie/recipe_molasses.html',
                    cookie_sku='MOL01',
                    quantity=1,
                    unit_cost=0.80)
    db.session.add(dcc)
    db.session.add(mol)
    db.session.flush()
    print(dcc.cookie_id)
    print(mol.cookie_id)

    # bulk_save_objects. fast insert data
    c1 = db.Cookie(cookie_name='peanut butter',
                   cookie_recipe_url='http://some.aweso.me/cookie/peanut.html',
                   cookie_sku='PB01',
                   quantity=24,
                   unit_cost=0.25)
    c2 = db.Cookie(cookie_name='oatmeal raisin',
                   cookie_recipe_url='http://some.okay.me/cookie/raisin.html',
                   cookie_sku='EWW01',
                   quantity=100,
                   unit_cost=1.00)
    db.session.bulk_save_objects([c1, c2])
    db.session.commit()
    print(c1.cookie_id)  # None


if __name__ == '__main__':
    init_insert()
