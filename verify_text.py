from .baseApp import Base
from selenium.webdriver.common.by import By
import sys
import os.path
libdir = os.path.dirname(__file__)
sys.path.append(os.path.split(libdir)[0])

class Locators:
    VERIFY_TEXT = (By.XPATH, "/html/body/section/div/div[4]/span")

class SearchVerifyText(Base):
    def search_text(self):
        return self.find_element(Locators.VERIFY_TEXT, time=2).text
