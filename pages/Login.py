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