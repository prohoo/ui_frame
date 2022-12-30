import csv
import os
import time
from pathlib import Path

import pytest
from core.pages import IndexPage, DealPage

#用wps新建的csv文件，要用记事本打开，另存为utf-8的格式，再复制到项目中，否则wps默认不是utf-8
#pytest -x -s 才能进行debugger模式  debgger(self.driver)

@pytest.mark.parametrize(
    "data",
    csv.DictReader(open("data_ddt/ddt_login.csv", encoding="utf-8-sig")),  #打开csv文件，读取到的值放到data中，此时data为字典
)

def test_login(driver,data):

    driver.get("http://47.107.116.139/fangwei/index.php")
    page = IndexPage(driver)  #实例化一个page  pom对象
    msg = page.login(data["用户名"],data["密码"])
    assert msg == data["登录结果"]
    # driver.quit()
    time.sleep(3)

def test_deal(driver):
    driver.get('http://47.107.116.139/fangwei/index.php?ctl=deal&id=21688')
    page = DealPage(driver)
    msg = page.pay(100,"msjy123")
    assert msg == "投标成功！"
    # driver.quit()
print(os.getcwd()+"@@")