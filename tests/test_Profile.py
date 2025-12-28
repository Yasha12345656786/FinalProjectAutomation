import allure
import pytest

from pages.Login import Login
from  pages.Profile import Profile
from tests.conftest import driver, set_up

@pytest.mark.Profile
@allure.suite("Profile")
def test_changeBgPic(set_up):
    driver = set_up
    l1 = Login(driver)
    p1 = Profile(driver)
    l1.Login("pabalemy@forexnews.bg", "weeer23")
    rtn = p1.changeBgPic()
    assert rtn == "css-1xlxqmr"

@pytest.mark.Profile
@allure.suite("Profile")
def test_changeProfilePic(set_up):
    driver = set_up
    l1 = Login(driver)
    p2 = Profile(driver)
    l1.Login("pabalemy@forexnews.bg", "weeer23")
    rtn = p2.changeProfilePic()
    assert rtn == True
#assert by attribute of class verify it is changed

@pytest.mark.Profile
@allure.suite("Profile")
def test_changeUsernameFromEditProfile(set_up):
    driver = set_up
    l = Login(driver)
    change0 = Profile(driver)
    l.Login("pabalemy@forexnews.bg", "weeer23")
    c = change0.changeUsernameFromEditProfile("test0088")
    assert c == "Username updated"

@pytest.mark.Profile
@allure.suite("Profile")
def test_changeCountryFromEditProfile(set_up):
    driver = set_up
    l = Login(driver)
    change1 = Profile(driver)
    l.Login("pabalemy@forexnews.bg", "weeer23")
    rtn = change1.changeCountryFromEditProfile()
    assert  rtn == "Brazil"

@pytest.mark.Profile
@allure.suite("Profile")
def test_chnageBdayFromEditProfile(set_up):
    driver = set_up
    l = Login(driver)
    change2 = Profile(driver)
    l.Login("pabalemy@forexnews.bg", "weeer23")
    rtn = change2.chnageBdayFromEditProfile()
    assert rtn == 'November 28, 1940'

@pytest.mark.Profile
@allure.suite("Profile")
def test_changeGenderFromEditProfile(set_up):
    driver = set_up
    l = Login(driver)
    change3 = Profile(driver)
    l.Login("pabalemy@forexnews.bg", "weeer23")
    rtn = change3.changeGenderFromEditProfile()
    assert rtn == "Other"

@pytest.mark.Profile
@allure.suite("Profile")
def test_changeProfilePicFromEditProfile(set_up):
    driver = set_up
    l = Login(driver)
    change4 = Profile(driver)
    l.Login("pabalemy@forexnews.bg", "weeer23")
    rtn = change4.changeProfilePicFromEditProfile()
    assert rtn == 'css-1kayl5r'

@pytest.mark.Profile
@allure.suite("Profile")
def test_changeBgPicFromEditProfile(set_up):
    driver = set_up
    l = Login(driver)
    change5 = Profile(driver)
    l.Login("pabalemy@forexnews.bg", "weeer23")
    rtn = change5.changeBgPicFromEditProfile()
    assert rtn == True

@pytest.mark.Profile
@allure.suite("Profile")
def test_changeProfileDetailsFromEditProfile(set_up):
    driver = set_up
    l = Login(driver)
    change6 = Profile(driver)
    l.Login("pabalemy@forexnews.bg", "weeer23")
    change6.changeProfileDetailsFromEditProfile("test0009")
