import allure
import pytest

from pages.CreatUser import SignUp
from tests.conftest import driver

@pytest.mark.CreateUser
@allure.suite("CreateUser")
def test_createUser(set_up):
    driver = set_up
    s1 = SignUp(driver)
    txt = s1.creatUser("hiwigitsae9w6s10@roa.com", "arrteawdess1234", "humanUsers0011")
    assert  txt == "Your account has been created!"
@pytest.mark.CreateUser
@allure.suite("CreateUser")
def test_InvalidEmail(set_up):
    driver = set_up
    s1 = SignUp(driver)
    n = s1.invalidEmail("sss")
    assert n == 1
@pytest.mark.CreateUser
@allure.suite("CreateUser")
def test_InvalidPassword(set_up):
    driver = set_up
    s1 = SignUp(driver)
    t = s1.invalidPassword("a", "1", "a1", "rndomandrto@walla.com")
    assert t == False
@pytest.mark.CreateUser
@allure.suite("CreateUser")
def test_InvalidUsername(set_up):
    driver = set_up
    s1 = SignUp(driver)
    t = s1.invalidUsername("!@#", "s23", "r4449!", "aaa1sdsesddffdfs2312112", "eeetdfeeswddffwr22@emfasl.com")
    assert t == False
@pytest.mark.CreateUser
@allure.suite("CreateUser")
def test_InvalidPresonalInfo(set_up):
    driver = set_up
    s1 = SignUp(driver)
    t = s1.invalidPresonalInfo("kmrwe@kmail.com", "P232D22sd", "dertwewel223")
    assert t == "You need to be 13 years or older to play on CrazyGames"
