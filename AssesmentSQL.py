import sqlite3

conn = sqlite3.connect('assesment.db')

c = conn.cursor()

c.execute("""CREATE TABLE brawlers (
            name TEXT,
            wallbreak TEXT,
            HP INTEGER,
            rarity TEXT,
            Year_Released INTEGER
            class TEXT
            )""")

conn.commit()
conn.close()
