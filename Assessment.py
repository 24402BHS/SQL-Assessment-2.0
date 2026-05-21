#imports
import sqlite3
#constants and variables
DATABASE = "Music.db"

#functions
def print_all_songs():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM songs;"
    cursor.execute(sql)
    result = cursor.fetchall()
    print("Name                               length in seconds")
    for songs in result:
        print(f"{songs[1]:<35}{songs[2]}")
    db.close

def print_all_albums():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM albums;"
    cursor.execute(sql)
    result = cursor.fetchall()
    print("Name                               Release Date        Explicit?")
    for albums in result:
        print(f"{albums[1]:<35}{albums[2]:<20}{albums[3]}")
    db.close

#main code
while True:
    user_input = input("\nWhat would you like to do?\n1. print all albums\n2. exit\n")
    if user_input == "1":
        print_all_albums()
    elif user_input == "2":
        break