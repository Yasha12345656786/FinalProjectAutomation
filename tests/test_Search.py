from tests.conftest import driver, set_up
from pages.Login import Login
from pages.Search import Search


def test_searchGame(set_up):
    driver = set_up
    l = Login(driver)
    s = Search(driver)
    l.Login("hiwigi9610@roastic.com", "wttew12445")
    rtn = s.searchForGame("Mario")
    assert rtn == "Mario"

