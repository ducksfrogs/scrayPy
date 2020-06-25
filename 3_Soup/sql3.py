import sqlite3

conn = sqlite3.connect('top_cities.db')

c = conn.cursor()
c.execute('DROP TABLE IF EXISTS cities')
c.execute("""
    CREATE TABLE cities (
        rank integer,
        city text,
        population integer
    )
""")

c.execute('INSERT INTO cities VALUES (?, ?, ?)',(1,'Shanhai', 2415000))
c.execute('INSERT INTO cities VALUES (:rank, :city, :population)',
        {'rank': 2, 'city': 'Karachi', 'population': 2350000})
c.executemany('INSERT INTO cities VALUES (:rank, :city, :population)', [
    {'rank': 3, 'city':'Beisin', 'population': 215000},
    {'rank': 4, 'city':'Tenshin', 'population': 14722},
    {'rank': 5, 'city':'Istanbool', 'population': 15000},
    ])
conn.commit()
c.execute('SELECT * FROM cities')
for row in c.fetchall():
    print(row)

conn.close()
