#imports
import sqlite3

#constants and variables
DATABASE = "Music.db"
Albums = "albums"
Songs = "songs"
Artists ="artists"
one = "1"
two = "2"
three = "3"
four = "4"
five = "5"
six = "6"

no1 = 1
no2 = 2
no3 = 3
no4 = 4
no5 = 5
no6 = 6

#functions
def print_all_songs():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    print_songs = "SELECT * FROM songs;"
    cursor.execute(print_songs)
    result = cursor.fetchall()
    print("Name                               length in seconds")
    for songs in result:
        print(f"{songs[1]:<35}{songs[2]}")
    sorting_songs()
    db.close

def print_all_albums():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    print_albums = "SELECT * FROM albums;"
    cursor.execute(print_albums)
    result = cursor.fetchall()
    print("Name                               Release Date        Explicit?")
    for albums in result:
        print(f"{albums[1]:<35}{albums[2]:<20}{albums[3]}")
    db.close

def print_all_artists():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    print_artists = "SELECT * FROM artists;"
    cursor.execute(print_artists)
    result = cursor.fetchall()
    print("Name")
    for artists in result:
        print(f"{artists[1]}")
    db.close

def search_by_artists():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    while True:
        try:
            artist_name = int(input('''What artist would you like to search?\n1. The Beatles\n2. Taylor Swift\n3. Adele\n4. Olivia Rodrigo\n5. Queen\n6. Bad Bunny\n'''))
            if artist_name == no1:
                artist_albums = "SELECT Albums.name FROM Artists INNER JOIN Albums ON Artists.id = Albums.artist_id WHERE Artists.id = 1"
                break
            elif artist_name == no2:
                artist_albums = "SELECT Albums.name FROM Artists INNER JOIN Albums ON Artists.id = Albums.artist_id WHERE Artists.id = 2"
                break
            elif artist_name == no3:
                artist_albums = "SELECT Albums.name FROM Artists INNER JOIN Albums ON Artists.id = Albums.artist_id WHERE Artists.id = 3"
                break
            elif artist_name == no4:
                artist_albums = "SELECT Albums.name FROM Artists INNER JOIN Albums ON Artists.id = Albums.artist_id WHERE Artists.id = 4"
                break
            elif artist_name == no5:
                artist_albums = "SELECT Albums.name FROM Artists INNER JOIN Albums ON Artists.id = Albums.artist_id WHERE Artists.id = 5"
                break
            elif artist_name == no6:
                artist_albums = "SELECT Albums.name FROM Artists INNER JOIN Albums ON Artists.id = Albums.artist_id WHERE Artists.id = 6"
                break
            else:
                print("Please choose a number")
        except ValueError:
            print("Please choose a number")
    cursor.execute(artist_albums)
    result = cursor.fetchall()
    for items in result:
        print(f"{items[0]}")
    db.close

def sorting_songs():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sorting_how = input("\nSort in what order?\nlength\nalphabetically\n")
    if sorting_how == "length":
        sort_songs = "SELECT name, length FROM Songs ORDER BY length DESC"
    elif sorting_how == "alphabetically":
        sort_songs = "SELECT name, length FROM Songs ORDER BY name DESC"
    cursor.execute(sort_songs)
    result = cursor.fetchall()
    for items in result:
        print(f"{items[0]:<35}{items[1]}")
    db.close
#sort the albums alphabetically and by length
def sorting_albums():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sorting_how = input("\nSort in what order?\nrelease date\nalphabetically\n")
    if sorting_how == "length":
        sort_albums = "SELECT name, release, explicit FROM Albums ORDER BY length DESC"
    elif sorting_how == "alphabetically":
        sort_albums = "SELECT name, length FROM Albums ORDER BY name DESC"
    cursor.execute(sort_albums)
    result = cursor.fetchall()
    for items in result:
        print(f"{items[0]:<35}{items[1]}")
    db.close

#main code
while True:
    try:
        user_input = input("\nWhat would you like to do?\n1. print albums\n2. print songs\n3. print artists\n4. more options\n")
        if user_input == one:
            print_all_albums()   
        elif user_input == two:
            print_all_songs()
        elif user_input == three:
            print_all_artists()
        elif user_input == four:
            more_options = input("\nHere you go\n5. exit\n6. search by artists\n")
            if more_options == six:
                search_by_artists()
            elif more_options == five:
                break
    except ValueError:
        print("Please choose one")