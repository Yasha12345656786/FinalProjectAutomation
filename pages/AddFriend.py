from pages.base_page import Base
from selenium.webdriver.common.by import By
from selenium import webdriver


class AddFriend(Base):
    def __init__(self, driver):
        self.driver: webdriver = driver
        super().__init__(driver)


    addFriendTab = (By.XPATH, "//div[@data-testid='header-friends-button']//button")
    friendSearchBox = (By.ID, "friends-search-input")
    addFriendBtn = (By.XPATH, "//button[contains(.,'Add')]")
    acceptFriendBtn = (By.XPATH, "//div[2]//div[2]//button[2]")


    def Addfriend(self, friendsUsername):
        self.clicky(self.addFriendTab)
        self.clicky(self.friendSearchBox)
        self.typeru(self.friendSearchBox, friendsUsername)
        self.wait_and_click(self.addFriendBtn)


    def acceptFriendRequest(self):
        self.clicky(self.addFriendTab)
        self.wait_for_visibility(self.acceptFriendBtn)
        self.clicky(self.acceptFriendBtn)



