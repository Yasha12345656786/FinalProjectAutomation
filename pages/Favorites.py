from selenium import webdriver
from pages.base_page import Base
from selenium.webdriver.common.by import By


class Favorites(Base):
    def __init__(self, driver):
        self.driver: webdriver = driver
        super().__init__(driver)

    game0 = (By.XPATH, "//a[@aria-label='Archer Ragdoll Masters']")
    gameFrame = (By.ID, "game-iframe")
    addToFav = (By.XPATH, "//div[@class='MuiGrid-root MuiGrid-item css-1sv96h7']//button")
    FavBtn = (By.XPATH, "//button[@aria-label='My Games']")
    favoriteGames = (By.XPATH, "//button[@tabindex='-1'][1]")
    game01 = (By.XPATH, "//div[@class='GameThumb_closeBtnContainer__84qjx']")
    verify = (By.XPATH, "//div[3]//div[contains(.,'Add games to your favorites by clicking on the ♡ icon on a game page.')]")

    def AddGameToFvaorites(self):
        self.clicky(self.game0)
        self.switch(self.gameFrame)
        self.waitpls()
        self.clicky(self.addToFav)
        rtn = self.GetAttr(self.addToFav)
        return rtn

    def RemoveGameFromFavorites(self):
        self.clicky(self.FavBtn)
        self.clicky(self.favoriteGames)
        self.clicky(self.game01)
        rtn = self.getText(self.verify)
        return rtn



