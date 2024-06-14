'''
Brawl Stars database application by William Li Chen

'''
# imports
import sqlite3

# constants and variables
DATABASE = "assessment.db"

# functions


def print_all_brawlers():
    db = sqlite3.connect(DATABASE)
    conn = db.cursor()
    sql = "SELECT * FROM Brawlers ORDER BY ID"
    conn.execute(sql)
    result = conn.fetchall()    # loop through results, print it nicely
    print("ID   Wallbreak   Name           HP      Rarity ID   Year Released   Class ID")
    for brawler in result:
        print(f"{brawler[0]:<5}{brawler[1]:<12}{brawler[2]:<15}{brawler[3]:<8}{brawler[4]:<12}{brawler[5]:<16}{brawler[6]:<5}")
    db.close()


def print_wallbreak():
    db = sqlite3.connect(DATABASE)
    conn = db.cursor()
    sql = "SELECT * FROM Brawlers WHERE Wallbreak == 'Yes'"
    conn.execute(sql)
    result = conn.fetchall()    # loop through results, print it nicely
    print("ID   Wallbreak   Name           HP      Rarity ID   Year Released   Class ID")
    for brawler in result:
        print(f"{brawler[0]:<5}{brawler[1]:<12}{brawler[2]:<15}{brawler[3]:<8}{brawler[4]:<12}{brawler[5]:<16}{brawler[6]:<5}")
    db.close()


def print_new():
    db = sqlite3.connect(DATABASE)
    conn = db.cursor()
    sql = "SELECT * FROM Brawlers ORDER BY Year_Released desc"
    conn.execute(sql)
    result = conn.fetchall()    # loop through results, print it nicely
    print("ID   Wallbreak   Name           HP      Rarity ID   Year Released   Class ID")
    for brawler in result:
        print(f"{brawler[0]:<5}{brawler[1]:<12}{brawler[2]:<15}{brawler[3]:<8}{brawler[4]:<12}{brawler[5]:<16}{brawler[6]:<5}")
    db.close()


def print_og():
    db = sqlite3.connect(DATABASE)
    conn = db.cursor()
    sql = "SELECT * FROM Brawlers WHERE Year_Released == 2017"
    conn.execute(sql)
    result = conn.fetchall()    # loop through results, print it nicely
    print("ID   Wallbreak   Name           HP      Rarity ID   Year Released   Class ID")
    for brawler in result:
        print(f"{brawler[0]:<5}{brawler[1]:<12}{brawler[2]:<15}{brawler[3]:<8}{brawler[4]:<12}{brawler[5]:<16}{brawler[6]:<5}")
    db.close()


def print_high_HP():
    db = sqlite3.connect(DATABASE)
    conn = db.cursor()
    sql = "SELECT Name, HP FROM Brawlers ORDER BY HP desc;"
    conn.execute(sql)
    result = conn.fetchall()    # loop through results, print it nicely
    print("Brawler        HP")
    for brawler in result:
        print(f"{brawler[0]:<15}{brawler[1]:<5}")
    db.close()


def print_low_HP():
    db = sqlite3.connect(DATABASE)
    conn = db.cursor()
    sql = "SELECT Name, HP FROM Brawlers ORDER BY HP;"
    conn.execute(sql)
    result = conn.fetchall()    # loop through results, print it nicely
    print("Brawler        HP")
    for brawler in result:
        print(f"{brawler[0]:<15}{brawler[1]:<5}")
    db.close()


def print_under10000_HP():
    db = sqlite3.connect(DATABASE)
    conn = db.cursor()
    sql = "SELECT Name, HP FROM Brawlers WHERE HP < 10000 ORDER BY HP desc;"
    conn.execute(sql)
    result = conn.fetchall()    # loop through results, print it nicely
    print("Brawler        HP")
    for brawler in result:
        print(f"{brawler[0]:<15}{brawler[1]:<5}")
    db.close()


def print_no_wallbreak():
    db = sqlite3.connect(DATABASE)
    conn = db.cursor()
    sql = "SELECT * FROM Brawlers WHERE Wallbreak == 'No'"
    conn.execute(sql)
    result = conn.fetchall()    # loop through results, print it nicely
    print("ID   Wallbreak   Name           HP      Rarity ID   Year Released   Class ID")
    for brawler in result:
        print(f"{brawler[0]:<5}{brawler[1]:<12}{brawler[2]:<15}{brawler[3]:<8}{brawler[4]:<12}{brawler[5]:<16}{brawler[6]:<5}")
    db.close()


def print_kit():
    db = sqlite3.connect(DATABASE)
    conn = db.cursor()
    sql = "SELECT * FROM Brawlers WHERE Name == 'Kit'"
    conn.execute(sql)
    result = conn.fetchall()    # loop through results, print it nicely
    print("ID   Wallbreak   Name           HP      Rarity ID   Year Released   Class ID")
    for brawler in result:
        print(f"{brawler[0]:<5}{brawler[1]:<12}{brawler[2]:<15}{brawler[3]:<8}{brawler[4]:<12}{brawler[5]:<16}{brawler[6]:<5}")
    db.close()


def print_epic_wallbreak():
    db = sqlite3.connect(DATABASE)
    conn = db.cursor()
    sql = "SELECT * FROM Brawlers WHERE Wallbreak == 'Yes' AND Rarity_ID = 4"
    conn.execute(sql)
    result = conn.fetchall()    # loop through results, print it nicely
    print("ID   Wallbreak   Name           HP      Rarity ID   Year Released   Class ID")
    for brawler in result:
        print(f"{brawler[0]:<5}{brawler[1]:<12}{brawler[2]:<15}{brawler[3]:<8}{brawler[4]:<12}{brawler[5]:<16}{brawler[6]:<5}")
    db.close()


def print_legendary_assassin():
    db = sqlite3.connect(DATABASE)
    conn = db.cursor()
    sql = "SELECT * FROM Brawlers WHERE Rarity_ID == 6 AND Class_ID = 2"
    conn.execute(sql)
    result = conn.fetchall()    # loop through results, print it nicely
    print("ID   Wallbreak   Name           HP      Rarity ID   Year Released   Class ID")
    for brawler in result:
        print(f"{brawler[0]:<5}{brawler[1]:<12}{brawler[2]:<15}{brawler[3]:<8}{brawler[4]:<12}{brawler[5]:<16}{brawler[6]:<5}")
    db.close()


def brawl_stardle():
    pass


def custom_sql():
    user = input("Please enter a Username: ")  # username and password system
    if user == "Babel":
        password = input("Please enter your Password: ")
        if password == "password123":
            pass
            print("Please enter a valid SQL statement.")
            db = sqlite3.connect(DATABASE)
            try:  # try to do a custom sql statement
                conn = db.cursor()
                sql = input("")
                conn.execute(sql)
                result = conn.fetchall()   
                for brawler in result:
                    print(brawler)
                db.close()
            except:
                print("Please retry with a valid SQL statement.")  # except to catch errors




        else:
            print("Please enter a valid Password next time.")
    else:
        print("Please enter a valid Username next time.")


# main
while True:
    custom_sql()
