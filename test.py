from selenium.common.exceptions import TimeoutException

from .click_page import SearchClick
from .byclass_attr import SearchHelpClassAttr

def test_click(browser):
    resource = "click"
    page = SearchClick(browser)
    page.go_to_site(resource)
    page.click_button()

    button = page.click_button()
    assert button

def test_classattr(browser):
    resource = "classattr"
    page = SearchHelpClassAttr(browser)
    page.go_to_site(resource)

    page.click_button()
    page.switch_to_alert_accept()
    button = page.test_button()
    assert button
