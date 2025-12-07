from selenium import webdriver
from pages.base_page import Base
from selenium.webdriver.common.by import By

class Login(Base):

    def __init__(self, driver):
        self.driver: webdriver = driver
        super().__init__(driver)

    btn = (By.ID, "header-login-button")
    email = (By.ID, "email")
    btn2 = (By.XPATH, "//div[@class='__className_f9243e css-1f20jmh']//button[@class='css-sgrktn']")
    password = (By.XPATH, "//input[@type='password']")
    btn3 = (By.XPATH, "//button[@type='submit']")
    iPass = (By.XPATH, "//div[@class='Drawer_errorContainer__HxIJd']")
    forgotPass = (By.XPATH, "//button[contains(.,'Forgot')]")
    sendMail = (By.XPATH, "//button[contains(.,'Send')]")
    mailSent = (By.XPATH, "//div[@class='Drawer_titleContainer__Zf5_r']")


    def Login(self, mail, pw):
        self.wait_and_click(self.btn)
        self.typeru(self.email, mail)
        self.clicky(self.btn2)
        self.wait_for_visibility(self.password)
        self.clicky(self.password)
        self.typeru(self.password, pw)
        self.clicky(self.btn3)
        return self.wait_and_if_no_visability_continue(self.iPass)

    def InvalidLogin(self, mail, pw):
        self.wait_and_click(self.btn)
        self.typeru(self.email, mail)
        self.clicky(self.btn2)
        self.wait_for_visibility(self.password)
        self.clicky(self.password)
        self.typeru(self.password, pw)
        self.clicky(self.btn3)
        self.wait_for_visibility(self.iPass)
        txt = self.getText(self.iPass)
        return txt

    def ForgotPassword(self, mail):
        self.wait_and_click(self.btn)
        self.typeru(self.email, mail)
        self.clicky(self.btn2)
        self.wait_for_visibility(self.forgotPass)
        self.clicky(self.forgotPass)
        self.wait_for_visibility(self.sendMail)
        self.clicky(self.sendMail)
        self.wait_for_visibility(self.mailSent)
        txt = self.getText(self.mailSent)
        return txt


