import allure
import pytest

from pages.Login import Login
from pages.Favorites import Favorites
from tests.conftest import driver, set_up

@pytest.mark.Favorites
@allure.suite("Favorites")
def test_AddGameToFavorites(set_up):
    l = Login(driver)
    f = Favorites(driver)
    l.Login("pabalemy@forexnews.bg", "weeer23")
    rtn = f.AddGameToFvaorites()
    assert rtn == "MuiGrid-root MuiGrid-item css-1huw71v"
@pytest.mark.Favorites
@allure.suite("Favorites")
def test_RemoveGameFromFavorites(set_up):
    l = Login(driver)
    f = Favorites(driver)
    l.Login("eeetdfeeswddffwr22@emfasl.com", "aaa1sdsesddffdfs2312112")
    rtn = f.RemoveGameFromFavorites()
    assert rtn == "Add games to your favorites by clicking on the ♡ icon on a game page."
