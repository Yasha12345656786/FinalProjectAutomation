from tests.conftest import driver, set_up
from pages.Login import Login
from pages.Logout import Logout
from pages.Friends import Friends


def test_AddFriend(set_up):
    driver = set_up
    l = Login(driver)
    af = Friends(driver)
    l.Login("hiwigi9610@roastic.com", "wttew12445")
    rtn = af.Addfriend("humanUser0003")
    assert rtn == "No results found"



def test_acceptFriendRequest(set_up):
    driver = set_up
    l = Login(driver)
    af = Friends(driver)
    l.Login("hiwigitsa9610@roa.com", "arrteads1234")
    rtn = af.acceptFriendRequest()
    assert int(rtn) > 0


def test_declineFriendRequest(set_up):
    driver = set_up
    l = Login(driver)
    af = Friends(driver)
    l.Login("hiwigitsa9610@roa.com", "arrteads1234")
    rtn, brtn = af.declineFriendRequest()
    assert brtn == rtn


def test_cancelFriendRequest(set_up):
    driver = set_up
    l = Login(driver)
    af = Friends(driver)
    l.Login("hiwigitsa9610@roa.com", "arrteads1234")
    rtn = af.cancelSentFriendRequest("humanUser0000")
    assert rtn == "Invite your friends"