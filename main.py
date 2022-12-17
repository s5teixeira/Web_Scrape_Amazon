import sqlite3
import requests
from bs4 import BeautifulSoup
import web_page_scraper


# def connect_to_database():
def main():
    # NOT SURE IF THIS FUNCTION IS ACCURATE ####

    # connecting to a database
    db_connection = None
    try:
        # connecting to sqlite
        db_connection = sqlite3.connect('amazon_db.db')
        # the  cursor object
        db_cursor = db_connection.cursor()

        # call function to create table for each region
        db_cursor = create_tables(db_cursor)





        # commit all changes made to the database
        db_connection.commit()
        db_cursor.close()

    # catch any database errors
    except sqlite3.Error as db_error:
        print(f'A Database Error has occurred: {db_error}')

    finally:
        # close the database connection if there's an error
        if db_connection:
            db_connection.close()
            print('Database connection closed.')


def create_tables(db_cursor):
    # this function creates the 6 tables
    # OVER EAR HEADPHONES
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
    return db_cursor


def insert_into_table(db_cursor, table_name, record_tuple):
    #This function inserts the record into the corresponding table
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


if __name__ == '__main__':
    main()
