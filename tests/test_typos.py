import logging
from time import sleep

import pytest
from spellchecker import SpellChecker
import requests

from web_testing.basic_page import WebPage
from web_testing.the_internet_locators import TyposLocators


@pytest.fixture(scope="function")
def web_page():
    web_page = WebPage("Chrome")
    web_page.open_page(TyposLocators.main_url)
    yield web_page
    web_page.driver.quit()


def test_typos_page(web_page):
    response = requests.get(TyposLocators.main_url)
    assert response.status_code == 200


def test_typos_in_text_1_element(web_page):
    spell = SpellChecker()
    custom_words = ["won't.", "typo,"]
    for word in custom_words:
        spell.word_frequency.load_words([word])
    for i in range(5):
        web_page.refresh()
        sleep(2)
        text_1 = web_page.get_elements(*TyposLocators.text)[1].text
        words = text_1.split()
        typos = spell.unknown(words)
        if typos:
            print(f"There are typos in your code {typos}.")
        else:
            print("No typos found.")
