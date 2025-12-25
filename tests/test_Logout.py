import allure
import pytest

from pages.Logout import Logout
from tests.conftest import driver, set_up
from pages.Login import Login

@pytest.mark.Logout
@allure.suite("Logout")
def test_Logout(set_up):
    driver = set_up
    l = Login(driver)
    lo = Logout(driver)
    l.Login("pabalemy@forexnews.bg", "weeer23")
    rtn = lo.Logout()
    assert rtn == "Log in"
