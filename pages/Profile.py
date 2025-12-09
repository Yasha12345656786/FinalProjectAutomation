from time import sleep

from selenium import webdriver

from pages.Login import Login
from pages.base_page import Base
from selenium.webdriver.common.by import By

from tests.conftest import set_up


class Profile(Base):

    def __init__(self, driver):
        self.driver: webdriver = driver
        super().__init__(driver)

    btn0 = (By.XPATH, "//img[@alt='Avatar']")
    btn1 = (By.XPATH, "//a[@class='MainDrawer_myProfileLink__isyho']")
    editBgPicbtn = (By.XPATH, "//div[@class='UserProfileHeader_hoverIcon___o4zm UserProfileHeader_headerEditIcon__TwM_N']")
    bgPic0 = (By.XPATH, "//div[@class='css-13giskk'][11]")
    bgPicSelected = (By.XPATH, "//div[@class='css-13giskk'][11]//span[@class='css-19ywb4']z")
    extEditBgPic = (By.XPATH, "//button[@class='css-170mte2']")
    rtnEditProfileBtn = (By.XPATH, "//button[@class='css-14q163a']")
    changeUsernameBtn0 = (By.XPATH, "//div[@class='TextField_wrapper__rVcy9 TextField_hasOnClick__VuKxI']//input")
    changeUsernameInput0 = (By.XPATH, "//input[@class='TextField_textField__XUqJS']")
    saveUsername0 = (By.XPATH, "//button[contains(.,'Save')]")
    successfullyUpdatedUsernameMsg0 = (By.XPATH, "//div[@class='UpdateUsernameForm_container__LWKa_']/div[3]")
    editMyProfileBtn = (By.XPATH, "//div[@class='UserProfileTitleBar_editButtonContainer__E0kY_']//button")
    selChangeCountry = (By.XPATH, "//div[2]//div[2]//select")
    optChangeCountry = (By.XPATH, "//option[contains(.,'Brazil')]")
    currentProfilePic = (By.XPATH, "//div[@class='UserProfileAvatarContainer_avatarContainer__XfCy1 UserProfileAvatarContainer_isOwnPage__tHp4I']")
    editProfilePicBtn = (By.XPATH, "//div[@class='UserProfileAvatarContainer_hoverIcon__E5qja UserProfileAvatarContainer_avatarEditIcon__mawXe']")
    profilePicOpt = (By.XPATH, "//div[@class='css-sm10zo']//div[41]")
    chosenProfilePic =  (By.XPATH, "//div[@class='css-sm10zo']//div[40]//span[@class='css-19ywb4']")
    BdayBtn = (By.XPATH, "//label[contains(.,'Birthday')]")




    def changeBgPic(self):
        self.wait_and_click(self.btn0)
        self.wait_and_click(self.btn1)
        self.clicky(self.editBgPicbtn)
        self.MoveToElement(self.bgPic0)
        self.clicky(self.bgPic0)
        self.wait_for_visibility(self.bgPicSelected)
        rtn = self.wait_and_if_no_visability_continue(self.bgPicSelected)
        self.clicky(self.extEditBgPic)
        return rtn

    def changeProfilePic(self):
        self.wait_and_click(self.btn0)
        self.wait_and_click(self.btn1)
        self.MoveToElement(self.currentProfilePic)
        self.wait_and_click(self.currentProfilePic)
        # sleep(4)
        # self.wait_for_visibility(self.editProfilePicBtn)
        # self.MoveToElement(self.editProfilePicBtn)
        # self.clicky(self.editProfilePicBtn)
        self.MoveToElement(self.profilePicOpt)
        self.clicky(self.profilePicOpt)
        return self.wait_and_if_no_visability_continue(self.chosenProfilePic)




    def changeUsernameFromEditProfile(self, un):
        self.wait_and_click(self.btn0)
        self.wait_and_click(self.btn1)
        self.clicky(self.editMyProfileBtn)
        self.clicky(self.changeUsernameBtn0)
        self.typeru(self.changeUsernameInput0, un)
        self.clicky(self.saveUsername0)
        rtn = self.getText(self.successfullyUpdatedUsernameMsg0)
        self.clicky(self.rtnEditProfileBtn)
        return rtn

    def changeCountryFromEditProfile(self):
        self.wait_and_click(self.btn0)
        self.wait_and_click(self.btn1)
        self.clicky(self.editMyProfileBtn)
        self.clicky(self.selChangeCountry)
        self.MoveToElement(self.optChangeCountry)
        self.clicky(self.optChangeCountry)
        rtn = self.getText(self.optChangeCountry)
        return rtn

    def chnageBdayFromEditProfile(self):
        self.wait_and_click(self.btn0)
        self.wait_and_click(self.btn1)
        self.clicky(self.editMyProfileBtn)
        self.wait_and_click(self.BdayBtn)













