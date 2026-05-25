#imports
import sqlite3

#constants and variables
DATABASE = "Music.db"
Albums = "albums"
Songs = "songs"
Artists ="artists"

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

def print_all_artists():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM artists;"
    cursor.execute(sql)
    result = cursor.fetchall()
    print("Name")
    for artists in result:
        print(f"{artists[1]}")
    db.close

#main code
while True:
    try:
        user_input = input("\nWhat would you like to do?\n1. print albums\n2. more options\n3. exit\n")
        if user_input == "1":
            print_all_albums()
        elif user_input == "2":
            more_options = input("\nHere you go\n4. print songs\n5. search in songs\n6. print artists\n")
            if more_options == "4":
                print_all_songs()
            elif more_options == "5":
                user_search = input("What song would you like to search? ")
            elif more_options == "6":
                print_all_artists()
        elif user_input == "3":
            break
    except ValueError:
        print("Just choose one")