from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.base_page import Base

class SignUp(Base):

    def __init__(self, driver):
        self.driver : webdriver = driver
        super().__init__(driver)

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
    optCountry1 = (By.XPATH, "//div[2]/div[@class='css-jxltcv']/div[@class='Dropdown_selectWrapper__TdpR7']//option[1]")
    selGender = (By.XPATH, "//div[@class='AboutYouDrawer_inputWrapper__VCdBD'][1]")
    optGender = (By.XPATH, "//div[@class='AboutYouDrawer_inputWrapper__VCdBD'][1]//option[5]")
    selMonth = (By.XPATH, "//div[@class='AboutYouDrawer_inputWrapper__VCdBD'][2]//select[contains(.,'Month')]")
    optMonth = (By.XPATH, "//div[@class='AboutYouDrawer_inputWrapper__VCdBD'][2]//select[contains(.,'Month')]//option[4]")
    selDay = (By.XPATH, "//div[@class='AboutYouDrawer_inputWrapper__VCdBD'][2]//select[contains(.,'Day')]")
    optDay = (By.XPATH, "//div[@class='AboutYouDrawer_inputWrapper__VCdBD'][2]//select[contains(.,'Day')]//option[10]")
    selYear = (By.XPATH, "//div[@class='AboutYouDrawer_inputWrapper__VCdBD'][2]//select[contains(.,'Year')]")
    optYear = (By.XPATH, "//div[@class='AboutYouDrawer_inputWrapper__VCdBD'][2]//select[contains(.,'Year')]//option[30]")
    optYear1 = (By.XPATH, "//div[@class='AboutYouDrawer_inputWrapper__VCdBD'][2]//select[contains(.,'Year')]//option[14]")
    optYear2 = (By.XPATH, "//div[@class='AboutYouDrawer_inputWrapper__VCdBD'][2]//select[contains(.,'Year')]//option[8]")
    optYear3 = (By.XPATH, "//div[@class='AboutYouDrawer_inputWrapper__VCdBD'][2]//select[contains(.,'Year')]//option[2]")
    btn5 = (By.XPATH, "//div[@class='AboutYouDrawer_inputWrapper__VCdBD']//button")
    created = (By.XPATH, "//div[2]//div[2][contains(.,'Your account has been created!')]")
    btn6 = (By.XPATH, "//div[@class='Drawer_rootDrawerContainer__EpxqM']//div[4]//button")
    iEmail = (By.XPATH, "//div[@class='EmailTextField_errorMessage__MDLpx']")
    ipass0 = (By.XPATH, "//form[@class='Forms_form__KYPNf']//div[@class='TextField_errorRow__lmx5a'][1]")
    ipass1 = (By.XPATH, "//form[@class='Forms_form__KYPNf']//div[@class='TextField_errorRow__lmx5a'][2]")
    ipass2 = (By.XPATH, "//form[@class='Forms_form__KYPNf']//div[@class='TextField_errorRow__lmx5a'][3]")
    iusername0 = (By.XPATH, "//div[@class='TextField_errorRow__lmx5a TextField_hasError__3conj'][1]")
    iusername1 = (By.XPATH, "//div[@class='TextField_errorRow__lmx5a TextField_hasError__3conj'][2]")
    iPersonalInfo = (By.XPATH, "//div[@class='Drawer_errorContainer__HxIJd']")

    def creatUser(self, mail, pw, un):
        self.wait_and_click(self.btn)
        self.typeru(self.email, mail)
        self.clicky(self.btn2)
        self.wait_for_visibility(self.password)
        self.typeru(self.password, pw)
        self.typeru(self.conPassword, pw)
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

    def invalidEmail(self, mail):
        t = 0
        self.wait_and_click(self.btn)
        self.typeru(self.email, mail)
        self.wait_for_visibility(self.iEmail)
        txt = self.getText(self.iEmail)
        if txt == "Invalid email":
            t = 1
        else: t = 0
        return t

    def invalidPassword(self, pw0, pw1, pw2, mail):
        self.wait_and_click(self.btn)
        self.typeru(self.email, mail)
        self.clicky(self.btn2)
        self.wait_for_visibility(self.password)
        t = True
        for i in range(3):
            self.typeru(self.password, pw0)
            self.typeru(self.conPassword, pw0)
            self.clear(self.password)
            self.clear(self.conPassword)
            self.typeru(self.password, pw1)
            self.typeru(self.conPassword, pw1)
            self.clear(self.password)
            self.clear(self.conPassword)
            self.typeru(self.password, pw2)
            self.typeru(self.conPassword, pw2)
            t = self.checkClickability(self.btn3)
        return t

    def invalidUsername(self, un0, un1, un2, pw1, mail):
        self.wait_and_click(self.btn)
        self.typeru(self.email, mail)
        self.clicky(self.btn2)
        self.wait_for_visibility(self.password)
        self.typeru(self.password, pw1)
        self.typeru(self.conPassword, pw1)
        self.clicky(self.terms)
        self.clicky(self.btn3)
        self.wait_for_visibility(self.username)
        t = self.checkClickability(self.btn4)
        for i in range(3):
            self.typeru(self.username, un0)
            t = self.checkClickability(self.btn4)
            self.clear(self.username)
            self.typeru(self.username, un1)
            t = self.checkClickability(self.btn4)
            self.clear(self.username)
            self.typeru(self.username, un2)
            t = self.checkClickability(self.btn4)
        return t

    def invalidPresonalInfo(self, mail, pw, un):
        self.wait_and_click(self.btn)
        self.typeru(self.email, mail)
        self.clicky(self.btn2)
        self.wait_for_visibility(self.password)
        self.typeru(self.password, pw)
        self.typeru(self.conPassword, pw)
        self.clicky(self.terms)
        self.clicky(self.btn3)
        self.wait_for_visibility(self.username)
        self.typeru(self.username, un)
        self.clicky(self.btn4)
        self.wait_for_visibility(self.selCountry)
        self.clicky(self.selMonth)
        self.clicky(self.optMonth)
        self.clicky(self.selDay)
        self.clicky(self.optDay)
        self.clicky(self.optYear1)
        self.clicky(self.optYear2)
        self.clicky(self.optYear3)
        t = self.getText(self.iPersonalInfo)
        return t




