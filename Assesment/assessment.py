'''
Brawl Stars database application by William Li Chen

'''
#  imports
import sqlite3

#  constants and variables
DATABASE = "assessment.db"

#  functions


def print_all_brawlers():
    db = sqlite3.connect(DATABASE)
    conn = db.cursor()
    sql = "SELECT * FROM Brawlers ORDER BY ID"
    conn.execute(sql)
    result = conn.fetchall()    #  loop through results, print it nicely
    print("ID   Wallbreak   Name           HP      Rarity ID   Year Released   Class ID")
    for brawler in result:
        print(f"{brawler[0]:<5}{brawler[1]:<12}{brawler[2]:<15}{brawler[3]:<8}{brawler[4]:<12}{brawler[5]:<16}{brawler[6]:<5}")
    db.close()



def print_high_HP():
    db = sqlite3.connect(DATABASE)
    conn = db.cursor()
    sql = "SELECT Name, HP FROM Brawlers ORDER BY HP desc;"
    conn.execute(sql)
    result = conn.fetchall()    #  loop through results, print it nicely
    print("Brawler        HP")
    for brawler in result:
        print(f"{brawler[0]:<15}{brawler[1]:<5}")
    db.close()


#  main
print_all_brawlers()
