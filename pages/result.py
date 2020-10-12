from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class DuckducgoResultPage:
    DIV_LINKS = (By.CSS_SELECTOR, '#links > div')
    SEARCH_INPUT = (By.ID, 'search_form_input')

    @classmethod
    def PHRASE_RESULTS(cls, PHRASE):
        xpath = f"//div[@id='links']//*[contains(text(), '{PHRASE}')]"
        return (By.XPATH, xpath)

    def __init__(self, browser):
        self.browser = browser

    def link_div_count(self):
        link_divs = self.browser.find_elements(*self.DIV_LINKS)
        return len(link_divs)

    def phrase_result_count(self,phrase):
        phrases = self.browser.find_elements(*self.PHRASE_RESULTS(phrase))
        return len(phrases)

    def search_input_value(self):
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        return search_input.get_attribute('value')