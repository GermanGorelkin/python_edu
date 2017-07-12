import sqlite3


conn = sqlite3.connect('example.db')
cur = conn.cursor()

# CREATE DB, TABLE and INSERT DATA
# cur.execute('''CREATE TABLE IF NOT EXISTS stocks
#             (date text, trans text, symbol text, qty real, price real)''')
#
# cur.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")
#
# conn.commit()

# purchases = [('2006-03-28', 'BUY', 'IBM', 1000, 45.00),
#              ('2006-04-05', 'BUY', 'MSFT', 1000, 72.00),
#              ('2006-04-06', 'SELL', 'IBM', 500, 53.00),
#             ]
# cur.executemany('INSERT INTO stocks VALUES (?,?,?,?,?)', purchases)
# conn.commit()

# cur.executescript("INSERT INTO stocks VALUES('2006-03-28', 'BUY', 'IBM', 1000, 45.00);"
#                   "INSERT INTO stocks VALUES('2006-03-28', 'BUY', 'IBM', 1000, 45.00);")
# conn.commit()

# for row in cur.execute('SELECT * FROM stocks ORDER BY price'):
#         print(row)

# t = ('RHAT',)
# cur.execute('SELECT * FROM stocks WHERE symbol=?', t)
# print(cur.fetchone())

conn.close()
