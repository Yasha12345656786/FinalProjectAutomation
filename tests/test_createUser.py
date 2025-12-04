from conftest import set_up
from pages.CreateUser import SignUp


def test_createUser(set_up):
    driver = set_up
    s1 = SignUp(driver)
    txt = s1.createUser("iconicOctopus2000@gmail.com", "pewpewmfer12", "pewpewmfer12", "yeepeekayey212")
    assert txt == "Your account has been created!"