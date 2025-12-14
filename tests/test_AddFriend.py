from tests.conftest import driver, set_up
from pages.Login import Login
from pages.Logout import Logout
from pages.AddFriend import AddFriend


def test_AddFriend(set_up):
    driver = set_up
    l = Login(driver)
    lo = Logout(driver)
    af = AddFriend(driver)
    l.Login("hiwigi9610@roastic.com", "wttew12445")
    af.Addfriend("humanUser0002")
    lo.Logout()
    l.Login("hiwigi9610@roa.com", "arrte1234")
    af.acceptFriendRequest()



