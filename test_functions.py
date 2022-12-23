import sqlite3

import pytest

import filter
import web_page_scraper

"""this module contains all the test functions """


def test_questions_about_filtering():
    """this function tests the questions about filtering function"""
    with pytest.raises(TypeError) as exception_info:
        assert filter.questions_about_filtering(float(4.5)) is True
        assert filter.questions_about_filtering('', False)
        assert filter.questions_about_filtering('No') is True
        assert filter.questions_about_filtering('Mac') is True
    assert exception_info.type is TypeError


def test_connect_to_db(capfd):
    """this function creates a fake database and makes sure it connects to it"""
    test_db = 'test_db.db'
    sqlite3.connect(test_db)


def test_search_selection():
    """This function tests the search selection function"""
    with pytest.raises(OSError) as error:
        filter.search_selection('3') is True
        filter.search_selection('0') is False
        filter.search_selection('Hello') is False
        filter.search_selection('') is False
        filter.search_selection('10') is False
        filter.search_selection('2') is True
    assert error.type is OSError


@pytest.fixture()
def cursor():
    """This function tests a connection and cursor object from one of the tables """
    connection = sqlite3.connect("test_db.db")
    cursor = connection.cursor()
    web_page_scraper.get_search_url(cursor, 'Over_Ear_Headphones_Table', 'over ear headphones')
    yield cursor
    cursor.execute('drop table Over_Ear_Headphones_Table')


def test_create_sql(cursor):
    """ This function tests the cursor function above, uses yielded/return value in this function,
    after test goes back to cursor() and deletes the table that it created"""
    table = 'Over_Ear_Headphones_Table'
    filter.questions_about_filtering(cursor, table)
    filter.sqlfunction(cursor, table, 4.0, '>', 1, '>', 1, '>')
