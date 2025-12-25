from pages.Login import Login
from pages.Favorites import Favorites
from tests.conftest import driver, set_up


def test_AddGameToFavorites(set_up):
    l = Login(driver)
    f = Favorites(driver)
    l.Login("pabalemy@forexnews.bg", "weeer23")
    rtn = f.AddGameToFvaorites()
    assert rtn == "MuiGrid-root MuiGrid-item css-1huw71v"
