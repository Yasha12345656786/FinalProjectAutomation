from pages.CreatUser import SignUp
from tests.conftest import driver


def test_createUser(set_up):
    driver = set_up
    s1 = SignUp(driver)
    txt = s1.creatUser("iconicOctou333s3200ssseee120@gmail.com", "pewpewe22czxreee1333332", "yepeeewwwwe222ey213332")
    assert  txt == "Your account has been created!"

def test_InvalidEmail(set_up):
    driver = set_up
    s1 = SignUp(driver)
    n = s1.invalidEmail("sss")
    assert n == 1

def test_InvalidPassword(set_up):
    driver = set_up
    s1 = SignUp(driver)
    t = s1.invalidPassword("a", "1", "a1", "rndomandrto@walla.com")
    assert t == False

def test_InvalidUsername(set_up):
    driver = set_up
    s1 = SignUp(driver)
    t = s1.invalidUsername("!@#", "s23", "r4449!", "aaa1sdsesddffdfs2312112", "eeetdfeeswddffwr22@emfasl.com")
    assert t == False

def test_InvalidPresonalInfo(set_up):
    driver = set_up
    s1 = SignUp(driver)
    t = s1.invalidPresonalInfo("kmrwe@kmail.com", "P232D22sd", "dertwewel223")
    assert t == "You need to be 13 years or older to play on CrazyGames"
