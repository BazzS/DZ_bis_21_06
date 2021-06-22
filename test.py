from selenium.common.exceptions import TimeoutException

from .click_page import SearchClick
from .byclass_attr import SearchHelpClassAttr
from .client_delay import SearchHelpClientDelay
from .dinamic_table import SearchDynamicTable
from .sample_app import SearchSampleApp
from .hidden_layers import SearchHiddenLayers
from .verify_text import SearchVerifyText
from .mouse_over import SearchMouseOver

import time


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

def test_clientdelay(browser):
    resource = "clientdelay"
    page = SearchHelpClientDelay(browser)
    page.go_to_site(resource)

    page.click_button()
    button = page.wait_to_text()
    assert button

def test_dinamictable(browser):
    resource = "dynamictable"
    page = SearchDynamicTable(browser)
    page.go_to_site(resource)

    chrome_cpu = page.chrome_cpu()
    tasks = page.tasks()
    list_task = tasks.text.split("\n")
    chrome_task = [chrome for chrome in list_task if chrome.startswith("Chrome")]
    chrome_detail_list = chrome_task[0].split()
    cpu = [cpu for cpu in chrome_detail_list if '%' in cpu]
    assert chrome_cpu == f'{chrome_detail_list[0]} CPU: {cpu[0]}'


def test_hidden_layers(browser):
    resource = "hiddenlayers"
    page = SearchHiddenLayers(browser)
    page.go_to_site(resource)

    first_click = page.click_button()
    assert first_click

    second_click = page.click_button()
    assert not second_click

def test_vefity_text(self):
    resource = "verifytext"
    page = SearchVerifyText(browser)
    page.go_to_site(resource)

    text = page.search_text()
    assert text == "Welcome UserName!"

def test_mouseover(self):
    resource = "mouseover"
    page = SearchMouseOver(browser)
    page.go_to_site(resource)

    first = page.find_click_count()
    page.double_clicl_link()
    second = page.find_click_count()
    assert (int(first) - int(second)) == 2
