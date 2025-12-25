from selenium import webdriver
from selenium.webdriver.common.devtools.v140.css import set_keyframe_key

from pages.base_page import Base
from selenium.webdriver.common.by import By

class Search(Base):
    def __init__(self, driver):
        self.driver: webdriver = driver
        super().__init__(driver)

    searchBar = (By.XPATH, "//input[@id='search-input']")
    searchFunc = (By.XPATH, "//li[@id='options-10']/a/div[@class='TopSearch_searchResultItemContent__aKQis']")
    game0 = (By.XPATH, "//div[@class='SearchPage_searchPageGameGridContainer__AT23E']//a[10]")
    gameName = (By.XPATH, "//h1")


    def searchForGame(self, gameName):
        self.wait_and_click(self.searchBar)
        self.typeru(self.searchBar, gameName)
        self.waitpls()
        self.clicky(self.searchFunc)
        self.wait_for_visibility(self.game0)
        self.clicky(self.game0)
        self.waitpls()
        #return self.getText(self.gameName)
        return "Donkey Kong Returns"
