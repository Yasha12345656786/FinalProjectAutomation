from selenium import webdriver
from time import sleep
import pyautogui
import pytest
from selenium.webdriver.common.by import By
from pages.base_page import Base


class SignUp(Base):

    def __init__(self, driver):
        self.driver : webdriver = driver

    btn = (By.ID, "header-login-button")
    email = (By.ID, "email")
    btn2 = (By.XPATH, "//div[@class='__className_f9243e css-1f20jmh']//button[@class='css-sgrktn']")
    password = (By.XPATH, "//div[@class='TextField_wrapper__rVcy9 TextField_endAdorned__MdZ_v'][1]//input[@class='TextField_textField__XUqJS TextField_hasLabel__8fiac']")
    conPassword = (By.XPATH, "//div[@class='TextField_wrapper__rVcy9 TextField_endAdorned__MdZ_v'][2]//input[@class='TextField_textField__XUqJS TextField_hasLabel__8fiac']")
    terms =  (By.XPATH, "//label[@class='MuiFormControlLabel-root MuiFormControlLabel-labelPlacementEnd Forms_acceptTncFormControl___w0G7 css-14ytr6n']//input")
    btn3 = (By.XPATH, "//div[@class='Drawer_rootDrawer__4N3VT SignIn_signUpEmailDrawer__73LNu']//button")
    username = (By.XPATH, "//div[@class='css-sm10zo']//input[@class='TextField_textField__XUqJS TextField_hasError__3conj']")
    btn4 = (By.XPATH, "//div[@class='css-sm10zo']//button")
    selCountry = (By.XPATH, "//div[2]/div[@class='css-jxltcv']/div[@class='Dropdown_selectWrapper__TdpR7']")
    optCountry = (By.XPATH, "//div[2]/div[@class='css-jxltcv']/div[@class='Dropdown_selectWrapper__TdpR7']//option[44]")
    selGender = (By.XPATH, "//div[@class='AboutYouDrawer_inputWrapper__VCdBD'][1]")
    optGender = (By.XPATH, "//div[@class='AboutYouDrawer_inputWrapper__VCdBD'][1]//option[5]")
    selMonth = (By.XPATH, "//div[@class='AboutYouDrawer_inputWrapper__VCdBD'][2]//select[contains(.,'Month')]")
    optMonth = (By.XPATH, "//div[@class='AboutYouDrawer_inputWrapper__VCdBD'][2]//select[contains(.,'Month')]//option[4]")
    selDay = (By.XPATH, "//div[@class='AboutYouDrawer_inputWrapper__VCdBD'][2]//select[contains(.,'Day')]")
    optDay = (By.XPATH, "//div[@class='AboutYouDrawer_inputWrapper__VCdBD'][2]//select[contains(.,'Day')]//option[10]")
    selYear = (By.XPATH, "//div[@class='AboutYouDrawer_inputWrapper__VCdBD'][2]//select[contains(.,'Year')]")
    optYear = (By.XPATH, "//div[@class='AboutYouDrawer_inputWrapper__VCdBD'][2]//select[contains(.,'Year')]//option[30]")
    btn5 = (By.XPATH, "//div[@class='AboutYouDrawer_inputWrapper__VCdBD']//button")
    created = (By.XPATH, "//div[2]//div[2][contains(.,'Your account has been created!')]")
    btn6 = (By.XPATH, "//div[@class='Drawer_rootDrawerContainer__EpxqM']//div[4]//button")

    def createUser(self, mail, pw, cpw, un):
        self.wait_and_click(self.btn)
        self.typeru(self.email, mail)
        self.clicky(self.btn2)
        self.wait_for_visibility(self.password)
        self.typeru(self.password, pw)
        self.typeru(self.conPassword, cpw)
        self.clicky(self.terms)
        self.clicky(self.btn3)
        self.wait_for_visibility(self.username)
        self.typeru(self.username, un)
        self.clicky(self.btn4)
        self.wait_for_visibility(self.selCountry)
        self.clicky(self.selCountry)
        self.clicky(self.optCountry)
        self.clicky(self.selGender)
        self.clicky(self.optGender)
        self.clicky(self.selMonth)
        self.clicky(self.optMonth)
        self.clicky(self.selDay)
        self.clicky(self.optDay)
        self.clicky(self.selYear)
        self.clicky(self.optYear)
        self.clicky(self.btn5)
        self.wait_for_visibility(self.created)
        txt = self.getText(self.created)
        self.clicky(self.btn6)
        return txt
