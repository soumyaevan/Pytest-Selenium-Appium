import pytest

from pages.search import DuckducgoSearchPage
from pages.result import DuckducgoResultPage



def test_basic_duckduckgo_search(browser):
    PHRASE = 'Panda'

    searchPage = DuckducgoSearchPage(browser)
    searchPage.load()
    searchPage.search(PHRASE)

    resultPage = DuckducgoResultPage(browser)
    assert resultPage.link_div_count() > 0
    assert resultPage.phrase_result_count(PHRASE) > 0
    assert resultPage.search_input_value() == PHRASE