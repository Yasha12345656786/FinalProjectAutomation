from selenium import webdriver
from pages.base_page import Base
from selenium.webdriver.common.by import By

class Logout(Base):

    def __init__(self, driver):
        self.driver: webdriver = driver
        super().__init__(driver)

    btn0 = (By.XPATH, "//img[@alt='Avatar']")
    logOutBtn = (By.XPATH, "//button[contains(.,'Log')]")
    loginBtn = (By.ID, "header-login-button")


    def Logout(self):
        self.clicky(self.btn0)
        self.clicky(self.logOutBtn)
        self.wait_for_visibility(self.loginBtn)
        rtn = self.getText(self.loginBtn)
        return rtn