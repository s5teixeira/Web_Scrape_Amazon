import sqlite3
import requests
from bs4 import BeautifulSoup
import web_page_scraper


def main():
    # NOT SURE IF THIS FUNCTION IS ACCURATE ####
    db_connection = None
    # connecting to a database
    try:
        # connecting to sqlite
        db_connection = connect_to_db('amazon_db.db')
        # the  cursor object
        db_cursor = create_db_cursor(db_connection)
        # call function to create table for each item
        db_cursor = create_tables(db_cursor)

        open("output_data.txt", "w").write("")
        web_page_scraper.get_search_url(db_cursor, 'USB_Microphones_Table', 'usb microphones')

    except sqlite3.Error as db_error:
        print(f'A Database Error has occurred: {db_error}')
    finally:
        # close the database connection whether there's an error or not
        if db_connection:
            db_connection.commit()
            db_connection.close()
            print('Database connection closed.')
            # deletes old text file and creates another each time its run
            # open("output_data.txt", "w")


def connect_to_db(amazon_db: str):
    db_connection = None
    try:
        db_connection = sqlite3.connect(amazon_db)
        print_green('connection to database was successful :)')
    except sqlite3.Error as db_error:
        print_red(f'{db_error}: connection to database was unsuccessful :(')
    finally:
        return db_connection


def create_db_cursor(db_connection_obj: sqlite3.Connection):
    cursor_obj = None
    try:
        cursor_obj = db_connection_obj.cursor()
        print_green(f'cursor object created successfully on {db_connection_obj}\n')
        # ) f'cursor object: {cursor_obj}')
    except sqlite3.Error as db_error:
        print_red(f'cursor object could not be created: {db_error}')
    finally:
        return cursor_obj


def create_tables(db_cursor):
    # this function creates the 6 tables **** could probably shorten it with a for loop
    # OVER EAR HEADPHONES
    try:
        db_cursor.execute('''CREATE TABLE IF NOT EXISTS Over_Ear_Headphones_Table(
                                product_name TEXT,
                                rating REAL,
                                num_ratings INTEGER,
                                price REAL,
                                product_url TEXT);''')
        db_cursor.execute('DELETE FROM Over_Ear_Headphones_Table')
        # USB MICROPHONES
        db_cursor.execute('''CREATE TABLE IF NOT EXISTS USB_Microphones_Table(
                                product_name TEXT,
                                rating REAL,
                                num_ratings INTEGER,
                                price REAL,
                                product_url TEXT);''')
        db_cursor.execute('DELETE FROM USB_Microphones_Table')
        # WEBCAMS
        db_cursor.execute('''CREATE TABLE IF NOT EXISTS Webcams_Table(
                                product_name TEXT,
                                rating REAL,
                                num_ratings INTEGER,
                                price REAL,
                                product_url TEXT);''')
        db_cursor.execute('DELETE FROM Webcams_Table')
        # CAPTURE CARDS
        db_cursor.execute('''CREATE TABLE IF NOT EXISTS Capture_Cards_Table(
                                product_name TEXT,
                                rating REAL,
                                num_ratings INTEGER,
                                price REAL,
                                product_url TEXT);''')
        db_cursor.execute('DELETE FROM Capture_Cards_Table')
        # AUDIO MIXERS
        db_cursor.execute('''CREATE TABLE IF NOT EXISTS Audio_Mixers_Table(
                                product_name TEXT,
                                rating REAL,
                                num_ratings INTEGER,
                                price REAL,
                                product_url TEXT);''')
        db_cursor.execute('DELETE FROM Audio_Mixers_Table')
        # GAMING LAPTOPS
        db_cursor.execute('''CREATE TABLE IF NOT EXISTS Gaming_Laptops_Table(
                                product_name TEXT,
                                rating REAL,
                                num_ratings INTEGER,
                                price REAL,
                                product_url TEXT);''')
        db_cursor.execute('DELETE FROM Gaming_Laptops_Table')
        print_green('tables created successfully')
    except sqlite3.Error as error:
        print_red('an error has occurred creating the tables :(')
        print_red(f'{error}')
    finally:
        return db_cursor


def insert_into_table(db_cursor, table_name, record_tuple):
    # This function inserts the record into the corresponding table
    if table_name == "Over_Ear_Headphones_Table":
        db_cursor.execute('''INSERT INTO Over_Ear_Headphones_Table VALUES(?, ?, ?, ?,?)''',
                          record_tuple)
    if table_name == "USB_Microphones_Table":
        db_cursor.execute('''INSERT INTO USB_Microphones_Table VALUES(?, ?, ?, ?,?)''',
                          record_tuple)
    if table_name == "Webcams_Table":
        db_cursor.execute('''INSERT INTO Webcams_Table VALUES(?, ?, ?, ?,?)''',
                          record_tuple)
    if table_name == "Capture_Cards_Table":
        db_cursor.execute('''INSERT INTO Capture_Cards_Table VALUES(?, ?, ?, ?,?)''',
                          record_tuple)
    if table_name == "Audio_Mixers_Table":
        db_cursor.execute('''INSERT INTO Audio_Mixers_Table VALUES(?, ?, ?, ?,?)''',
                          record_tuple)
    if table_name == "Gaming_Laptops_Table":
        db_cursor.execute('''INSERT INTO Gaming_Laptops_Table VALUES(?, ?, ?, ?,?)''',
                          record_tuple)
    return db_cursor


def print_red(text: str):
    """ this function changes lines printed to terminal red """
    print(f'\033[91m{text}')


def print_green(text: str):
    """ this function changes lines printed to terminal green """
    print(f'\033[92m{text}')


if __name__ == '__main__':
    main()
