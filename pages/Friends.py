from pages.base_page import Base
from selenium.webdriver.common.by import By
from selenium import webdriver


class Friends(Base):
    def __init__(self, driver):
        self.driver: webdriver = driver
        super().__init__(driver)


    addFriendTab = (By.XPATH, "//div[@data-testid='header-friends-button']//button")
    friendSearchBox = (By.ID, "friends-search-input")
    addFriendBtn = (By.XPATH, "//button[contains(.,'Add')]")
    friendAdded = (By.XPATH, "//div[@id='__next']/div/div[4]/div/div[2]/div/div/div[2]")
    acceptFriendBtn = (By.XPATH, "//div[2]//div[2]//button[2]")
    declineFriendBtn = (By.XPATH, "//div[2]//div[2]//button[1]")
    offlineFriendsAmount = (By.XPATH, "//div[2]//div[3]//span[@class='css-10jnuj1']")
    cancelFriendRequest = (By.XPATH, "//button[contains(.,'Cancel')]")
    noFriendRequests = (By.XPATH, "//div[2]//div[2][contains(.,'Invite your friends')]")


    def Addfriend(self, friendsUsername):
        self.clicky(self.addFriendTab)
        self.clicky(self.friendSearchBox)
        self.typeru(self.friendSearchBox, friendsUsername)
        self.wait_and_click(self.addFriendBtn)
        self.waitpls()
        return self.getText(self.friendAdded)


    def acceptFriendRequest(self):
        self.clicky(self.addFriendTab)
        self.wait_for_visibility(self.acceptFriendBtn)
        self.clicky(self.acceptFriendBtn)
        return self.getText(self.offlineFriendsAmount)

    def declineFriendRequest(self):
        brtn = int(self.getText(self.offlineFriendsAmount))
        self.clicky(self.addFriendTab)
        self.wait_for_visibility(self.acceptFriendBtn)
        self.clicky(self.declineFriendBtn)
        self.waitpls()
        rtn = int(self.getText(self.offlineFriendsAmount))
        return rtn, brtn



    def cancelSentFriendRequest(self, friendsUsername):
        self.clicky(self.addFriendTab)
        self.clicky(self.friendSearchBox)
        self.typeru(self.friendSearchBox, friendsUsername)
        self.wait_and_click(self.addFriendBtn)
        self.waitpls()
        self.clicky(self.cancelFriendRequest)
        self.waitpls()
        return self.getText(self.noFriendRequests)
