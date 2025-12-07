from pages.Login import Login
from tests.conftest import driver


def test_Login(set_up):
    driver = set_up
    l1 = Login(driver)
    t = l1.Login("eeetdfeeswddffwr22@emfasl.com", "aaa1sdsesddffdfs2312112")
    assert t == True

def test_InvalidLogin(set_up):
    driver = set_up
    l2 = Login(driver)
    t = l2.InvalidLogin("eeetdfeeswddffwr22@emfasl.com", "qwe122223")
    assert t == "The password you entered is incorrect."


def test_ForgotPassword(set_up):
    driver = set_up
    l3 = Login(driver)
    t = l3.ForgotPassword("pabalemy@forexnews.bg")
    assert t == "Mail sent!"
