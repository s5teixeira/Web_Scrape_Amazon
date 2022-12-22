
"""this module contains all the test functions """

#
# def test_Over_Ear_Headphones():
#     assert something ...
import sqlite3

import pytest

import web_page_scraper


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
    connection = sqlite3.connect("test_db.db")
    cursor = connection.cursor()
    # cursor.execute("CREATE TABLE Over_Ear_Headphones_Table(product_name TEXT, rating REAL, "
    #                "num_ratings INTEGER, price REAL, product_url TEXT)")
    web_page_scraper.get_search_url(cursor, 'Over_Ear_Headphones_Table', 'over ear headphones')
    yield cursor  # return database
    cursor.execute('drop table Over_Ear_Headphones_Table')


def test_create_sql(cursor):
    # uses cursor() function above uses yielded/return value in this function, after test goes back to cursor()
    # and deletes the table that it created.
    # set up and tear down - have to run function again with new database
    table = 'Over_Ear_Headphones_Table'
    filter.ask_question_create_sql(cursor, table, 4.0, '>', 1, '>', 1, '>')







