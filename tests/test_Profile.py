from pages.Login import Login
from  pages.Profile import Profile
from tests.conftest import driver, set_up


def test_changeBgPic(set_up):
    driver = set_up
    l1 = Login(driver)
    p1 = Profile(driver)
    l1.Login("pabalemy@forexnews.bg", "weeer23")
    rtn = p1.changeBgPic()
    assert rtn == True

def test_changeProfilePic(set_up):
    driver = set_up
    l1 = Login(driver)
    p2 = Profile(driver)
    l1.Login("pabalemy@forexnews.bg", "weeer23")
    rtn = p2.changeProfilePic()
    assert rtn == True


def test_changeUsernameFromEditProfile(set_up):
    driver = set_up
    l = Login(driver)
    change0 = Profile(driver)
    l.Login("pabalemy@forexnews.bg", "weeer23")
    c = change0.changeUsernameFromEditProfile("test0003")
    assert c == "Username updated"


def test_changeCountryFromEditProfile(set_up):
    driver = set_up
    l = Login(driver)
    change1 = Profile(driver)
    l.Login("pabalemy@forexnews.bg", "weeer23")
    rtn = change1.changeCountryFromEditProfile()
    assert  rtn == "Brazil"