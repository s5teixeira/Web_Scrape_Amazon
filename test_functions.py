"""this module contains all the test functions """
import sqlite3
import filter
import pytest

""" This is the automated unit test module for this project. 
Every function begins with test_, so python/pytest knows its used for testing """



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





