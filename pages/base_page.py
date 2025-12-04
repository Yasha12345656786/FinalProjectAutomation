from selenium import EC
from time import sleep
import pyautogui
import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

class Base:

    def __init__(self, driver):
        self.driver : webdriver = driver
        self.wait = WebDriverWait(self.driver, 5)

    def wait_for_element(self, locators):
        return self.wait.until(EC.presence_of_element_located(locators))

    def wait_for_visibility(self, locators):
        return self.wait.until(EC.visibility_of_element_located(locators))

    def wait_and_click(self, locators):
        self.wait.until(EC.visibility_of_element_to_be_clickable(locators)).click()
        sleep(1)

    def clicky(self, locators):
        element = self.driver.find_element(*locators)
        element.click()
        sleep(1)

    def clicke(self, locators):
        element = self.driver.find_element(locators)
        element.click()
        sleep(1)


    def getText(self, locators):
        element = self.driver.find_element(locators)
        txt = element.text
        return txt

    def typeru(self, locators, text):
        element = self.driver.find_element(*locators)
        element.clear()
        element.send_keys(text)

    def clear(self, locators):
        element = self.driver.find_element(*locators)
        element.clear()

    def switch(self, locators):
        element = self.driver.find_element(*locators)
        self.driver.switch_to.frame(element)