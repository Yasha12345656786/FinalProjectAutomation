from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import pyautogui
import pytest
from selenium.webdriver import ActionChains, Keys
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

    def wait_for_visibility1(self, locators):
        return self.wait.until(EC.visibility_of_element_located(*locators))

    def wait_and_if_no_visability_continue(self, locators):
        try:
            return self.wait.until(EC.visibility_of_element_located(locators))
        except TimeoutException as e:
            return True

    def wait_and_if_no_visability_continue1(self, locators):
        try:
            self.wait.until(EC.visibility_of_element_located(*locators))
            return False
        except TimeoutException as e:
            return True

    def waitpls(self):
        sleep(3)
    def wait_and_click(self, locators):
        self.wait.until(EC.element_to_be_clickable(locators)).click()
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
        element = self.driver.find_element(*locators)
        txt = element.text
        return txt

    def getColor(self, locators):
        element = self.driver.find_element(*locators)
        color = element.value_of_css_property("color")
        return color.text

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

    def checkClickability(self, locators):
        element = self.driver.find_element(*locators)
        a = element.is_enabled()
        return a

    def MoveToElement(self, locators):
        action = ActionChains(self.driver)
        element = self.driver.find_element(*locators)
        action.move_to_element(element)
        sleep(10)

    def PressEnter(self):
        action = ActionChains(self.driver)
        action.key_down(Keys.ENTER)
        action.key_up(Keys.ENTER)

    def GetAttrClass(self, locators):
        element = self.driver.find_element(*locators)
        return element.get_attribute("class")

    def GetAttrValue(self, locators):
        element = element = self.driver.find_element(*locators)
        return element.get_attribute("value")