import pytest
from selenium.webdriver.chrome import webdriver
from selenium import webdriver
# from webdriver_helper import get_webdriver

#
from core.funcs import load_cookies, save_cookies, is_login
from core.pages import AdminLoginPage

"""普通状态的driver"""
@pytest.fixture(scope="module")  # 要想所有用例在同一个浏览器执行，scope可改为最大范围，默认是最小的function
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(2)
    driver.maximize_window()
    yield driver  # 后置动作
    driver.quit()



"""登录过的driver：admin_driver"""


@pytest.fixture(scope="session")  # session作用域：当前会话/函数
def admin_driver():
    """创建一个已经登录过的driver，拿到cookies以便快速登录"""
    driver = webdriver.Chrome()
    # driver = get_webdriver()
    driver.implicitly_wait(5)
    driver.maximize_window()
    # 1. 先加载cookies
    load_cookies(driver)
    # 2. 再判断是否已经登录过
    if is_login(driver) is False:
        page = AdminLoginPage(driver)
        assert page.login('admin', 'msjy123') is True  # 会返回is_login值
        # assert is_login_flag == True  # 登录成功后,
        # 登录页面把admin_driver函数作为参数，给调用函数返回一个登录过的driver
    yield driver   # yield driver:通过yield返回浏览器（此时的driver已经登录过带上session了）
    save_cookies(driver)
    driver.quit()


"""不同账号的driver"""
# @pytest.fixture(scope="session")
# def other_driver():
