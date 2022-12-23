import sqlite3
import requests
from bs4 import BeautifulSoup
import filter
import web_page_scraper

"""This module deals with filtering data tables """


def main():
    """This function connects to the sqlite3 database and opens a text file """
    db_connection = None
    try:
        db_connection = connect_to_db('amazon_db.db')
        db_cursor = create_db_cursor(db_connection)
        db_cursor = call_to_create_all_tables(db_cursor)
        open("output_data.txt", "w").write("")
        open("filtered_data.txt", "w").write("")
        call_to_getsearchurl(db_cursor)
    except sqlite3.Error as db_error:
        print_red(f'A Database Error has occurred: {db_error}')
    finally:
        if db_connection:
            db_connection.commit()
            db_connection.close()
            print('\n\nDatabase connection closed.')


def call_to_getsearchurl(db_cursor):
    """This function calls the search url"""
    web_page_scraper.get_search_url(db_cursor, 'USB_Microphones_Table', 'usb microphones')
    web_page_scraper.get_search_url(db_cursor, 'Audio_Mixers_Table', 'audio mixers')
    web_page_scraper.get_search_url(db_cursor, 'Capture_Cards_Table', 'capture cards')
    web_page_scraper.get_search_url(db_cursor, 'Over_Ear_Headphones_Table', 'over ear headphones')
    web_page_scraper.get_search_url(db_cursor, 'Gaming_Laptops_Table', 'gaming laptop')
    web_page_scraper.get_search_url(db_cursor, 'Webcams_Table', 'webcam')
    filter.search_selection(db_cursor)


def ask_to_continue(db_cursor):
    """This function asks to continue filtering table to the user """
    print("\n\nkeep searching or exit?")
    param = input("select y or n >> ")
    if param == 'y':
        filter.search_selection(db_cursor)
    else:
        db_cursor.close()
        exit()


def connect_to_db(amazon_db: str):
    """" this function connects to the database"""
    db_connection = None
    try:
        db_connection = sqlite3.connect(amazon_db)
        print_green('connection to database was successful :)')
    except sqlite3.Error as db_error:
        print_red(f'{db_error}: connection to database was unsuccessful :(')
    finally:
        return db_connection


def create_db_cursor(db_connection_obj: sqlite3.Connection):
    """ this function creates the database cursor object"""
    cursor_obj = None
    try:
        cursor_obj = db_connection_obj.cursor()
        print_green(f'cursor object created successfully on {db_connection_obj}\n')
    except sqlite3.Error as db_error:
        print_red(f'cursor object could not be created: {db_error}')
    finally:
        return cursor_obj


def create_OverEarTable(db_cursor):
    """This function creates the Over Ear Headphones table"""
    try:
        db_cursor.execute('''CREATE TABLE IF NOT EXISTS Over_Ear_Headphones_Table(
                                product_name TEXT,
                                rating REAL,
                                num_ratings INTEGER,
                                price REAL,
                                product_url TEXT);''')
        db_cursor.execute('DELETE FROM Over_Ear_Headphones_Table')
    except sqlite3.Error as error:
        print_red('an error has occurred creating the tables :(')
        print_red(f'{error}')
    finally:
        return db_cursor


def create_MicTable(db_cursor):
    """This function creates the Microphone Table """
    try:
        db_cursor.execute('''CREATE TABLE IF NOT EXISTS USB_Microphones_Table(
                                product_name TEXT,
                                rating REAL,
                                num_ratings INTEGER,
                                price REAL,
                                product_url TEXT);''')
        db_cursor.execute('DELETE FROM USB_Microphones_Table')
    except sqlite3.Error as error:
        print_red('an error has occurred creating the tables :(')
        print_red(f'{error}')
    finally:
        return db_cursor


def create_WebTable(db_cursor):
    """This function creates the WebCams table"""
    try:
        db_cursor.execute('''CREATE TABLE IF NOT EXISTS Webcams_Table(
                                product_name TEXT,
                                rating REAL,
                                num_ratings INTEGER,
                                price REAL,
                                product_url TEXT);''')
        db_cursor.execute('DELETE FROM Webcams_Table')
    except sqlite3.Error as error:
        print_red('an error has occurred creating the tables :(')
        print_red(f'{error}')
    finally:
        return db_cursor


def create_CardsTable(db_cursor):
    """This function creates the Capture Cards table"""
    try:
        db_cursor.execute('''CREATE TABLE IF NOT EXISTS Capture_Cards_Table(
                                product_name TEXT,
                                rating REAL,
                                num_ratings INTEGER,
                                price REAL,
                                product_url TEXT);''')
        db_cursor.execute('DELETE FROM Capture_Cards_Table')
    except sqlite3.Error as error:
        print_red('an error has occurred creating the tables :(')
        print_red(f'{error}')
    finally:
        return db_cursor


def create_AudioTable(db_cursor):
    """This function creates the Audio Mixers Table """
    try:
        db_cursor.execute('''CREATE TABLE IF NOT EXISTS Audio_Mixers_Table(
                                product_name TEXT,
                                rating REAL,
                                num_ratings INTEGER,
                                price REAL,
                                product_url TEXT);''')
        db_cursor.execute('DELETE FROM Audio_Mixers_Table')
    except sqlite3.Error as error:
        print_red('an error has occurred creating the tables :(')
        print_red(f'{error}')
    finally:
        return db_cursor


def create_GamingTable(db_cursor):
    """This function creates the Gaming Laptops table"""
    try:
        db_cursor.execute('''CREATE TABLE IF NOT EXISTS Gaming_Laptops_Table(
                                product_name TEXT,
                                rating REAL,
                                num_ratings INTEGER,
                                price REAL,
                                product_url TEXT);''')
        db_cursor.execute('DELETE FROM Gaming_Laptops_Table')
    except sqlite3.Error as error:
        print_red('an error has occurred creating the tables :(')
        print_red(f'{error}')
    finally:
        return db_cursor


def call_to_create_all_tables(db_cursor):
    """This function calls all the created tables"""
    create_OverEarTable(db_cursor)
    create_MicTable(db_cursor)
    create_WebTable(db_cursor)
    create_CardsTable(db_cursor)
    create_AudioTable(db_cursor)
    create_GamingTable(db_cursor)
    print_green('tables created successfully')
    return db_cursor


def insert_into_OverEar(db_cursor, table_name, record_tuple):
    """This function inserts into Over Ear Headphones"""
    try:
        if table_name == "Over_Ear_Headphones_Table":
            db_cursor.execute('''INSERT INTO Over_Ear_Headphones_Table VALUES(?, ?, ?, ?,?)''',
                              record_tuple)
    except sqlite3.Error as error:
        print_red('an error has occurred while inserting the tables :(')
        print_red(f'{error}')
    finally:
        return db_cursor


def insert_into_Mic(db_cursor, table_name, record_tuple):
    """This function inserts into Microphone Table"""
    try:
        if table_name == "USB_Microphones_Table":
            db_cursor.execute('''INSERT INTO USB_Microphones_Table VALUES(?, ?, ?, ?,?)''',
                              record_tuple)
    except sqlite3.Error as error:
        print_red('an error has occurred while inserting the tables :(')
        print_red(f'{error}')
    finally:
        return db_cursor


def insert_into_Web(db_cursor, table_name, record_tuple):
    """This function inserts into Webcams table"""
    try:
        if table_name == "Webcams_Table":
            db_cursor.execute('''INSERT INTO Webcams_Table VALUES(?, ?, ?, ?,?)''',
                              record_tuple)
    except sqlite3.Error as error:
        print_red('an error has occurred while inserting the tables :(')
        print_red(f'{error}')
    finally:
        return db_cursor


def insert_into_Capture(db_cursor, table_name, record_tuple):
    """This function inserts into Capture cards table"""
    try:
        if table_name == "Capture_Cards_Table":
            db_cursor.execute('''INSERT INTO Capture_Cards_Table VALUES(?, ?, ?, ?,?)''',
                              record_tuple)
    except sqlite3.Error as error:
        print_red('an error has occurred while inserting the tables :(')
        print_red(f'{error}')
    finally:
        return db_cursor


def insert_into_Audio(db_cursor, table_name, record_tuple):
    """This function inserts into Audio Mixers Table"""
    try:
        if table_name == "Audio_Mixers_Table":
            db_cursor.execute('''INSERT INTO Audio_Mixers_Table VALUES(?, ?, ?, ?,?)''',
                              record_tuple)
    except sqlite3.Error as error:
        print_red('an error has occurred while inserting the tables :(')
        print_red(f'{error}')
    finally:
        return db_cursor


def insert_into_Gaming(db_cursor, table_name, record_tuple):
    """This function inserts into Gaming Laptops table"""
    try:
        if table_name == "Gaming_Laptops_Table":
            db_cursor.execute('''INSERT INTO Gaming_Laptops_Table VALUES(?, ?, ?, ?,?)''',
                              record_tuple)
    except sqlite3.Error as error:
        print_red('an error has occurred while inserting the tables :(')
        print_red(f'{error}')
    finally:
        return db_cursor


def calls_to_insert_all_tables(db_cursor, table_name, record_tuple):
    """This function calls all the tables """
    insert_into_OverEar(db_cursor, table_name, record_tuple)
    insert_into_Mic(db_cursor, table_name, record_tuple)
    insert_into_Web(db_cursor, table_name, record_tuple)
    insert_into_Capture(db_cursor, table_name, record_tuple)
    insert_into_Audio(db_cursor, table_name, record_tuple)
    insert_into_Gaming(db_cursor, table_name, record_tuple)


def print_red(text: str):
    """ this function changes lines printed to terminal red """
    print(f'\033[91m{text}')


def print_green(text: str):
    """ this function changes lines printed to terminal green """
    print(f'\033[92m{text}')


if __name__ == '__main__':
    main()
