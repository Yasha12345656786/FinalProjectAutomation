from selenium import webdriver
from pages.base_page import Base
from selenium.webdriver.common.by import By


class Favorites(Base):
    def __init__(self, driver):
        self.driver: webdriver = driver
        super().__init__(driver)

    game0 = (By.XPATH, "//a[@aria-label='Archer Ragdoll Masters']")
    gameFrame = (By.ID, "game-iframe")
    favBtn = (By.XPATH, "//div[@class='MuiGrid-root MuiGrid-item css-1sv96h7']//button")

    def AddGameToFvaorites(self):
        self.clicky(self.game0)
        self.switch(self.gameFrame)
        self.clicky(self.favBtn)
        rtn = self.GetAttr(self.favBtn)
        return rtn
