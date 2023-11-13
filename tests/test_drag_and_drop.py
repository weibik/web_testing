import pytest
from selenium.webdriver import ActionChains

from web_testing.basic_page import WebPage
from web_testing.the_internet_locators import DragAndDropLocators


@pytest.fixture(scope="function")
def web_page():
    web_page = WebPage("Chrome")
    web_page.open_page(DragAndDropLocators.main_url)
    yield web_page
    web_page.driver.quit()


def drag_and_drop_func(web_page, source, taret):
    script = """
            var source = arguments[0];
            var target = arguments[1];
            var event = new MouseEvent('mousedown', {
                bubbles: true,
                cancelable: true,
                view: window
            });
            source.dispatchEvent(event);

            event = new MouseEvent('mousemove', {
                bubbles: true,
                cancelable: true,
                view: window
            });
            source.dispatchEvent(event);

            event = new MouseEvent('mouseup', {
                bubbles: true,
                cancelable: true,
                view: window
            });
            target.dispatchEvent(event);
        """
    web_page.driver.execute_script(script, source, taret)


def test_drag_a_to_b(web_page):
    draggable_a = web_page.driver.find_element(*DragAndDropLocators.draggable_a)
    draggable_b = web_page.driver.find_element(*DragAndDropLocators.draggable_b)
    drag_and_drop_func(web_page, draggable_a, draggable_b)


def test_drag_b_to_a(web_page):
    draggable_a = web_page.driver.find_element(*DragAndDropLocators.draggable_a)
    draggable_b = web_page.driver.find_element(*DragAndDropLocators.draggable_b)
    drag_and_drop_func(web_page, draggable_b, draggable_a)


def test_using_actions(web_page):
    # Same test as "test_drag_a_to_b", but using Actions instead of javascript
    draggable_a = web_page.driver.find_element(*DragAndDropLocators.draggable_a)
    draggable_b = web_page.driver.find_element(*DragAndDropLocators.draggable_b)
    actions = ActionChains(web_page.driver)
    actions.drag_and_drop(draggable_a, draggable_b).perform()
