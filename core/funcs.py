import json
import os
from pathlib import Path

import requests

import requests


##后台的登录处理

# 无论在哪里执行，它都是获取的当前文件的绝对路径,但会带上testcases,所以要跨目录的情况不适用，用os.getcmd()
# cuurent_path = str(Path(__file__).parent)


# chaojiying.com识别验证码,使用原理：先对验证码进行截图driver.find_element(By.XPATH, '//*[@id="verify"]').screenshot("verify.png")
# 再对所截图进行post请求识别，返回在验证码在pic_str中
def img2code(files):
    url = "http://upload.chaojiying.net/Upload/Processing.php"
    files = {"userfile": open(files, "rb")}
    data = {
        "user": "helang007",
        "pass2": "6d72c1b6f73f0c9530fe729ec9e61d2d",  # MD5加密后的密码  @@mima0077
        "codetype": 1902  # 识别图形的格式：https://www.chaojiying.com/price.html
    }
    resp = requests.post(url=url, files=files, data=data)
    res = resp.json()
    if res["err_no"] == 0:
        code = res["pic_str"]  # 超级鹰识别成功后保存在所返回的pic_str中
        print("识别成功：{}".format(code))
        return code
    else:
        print("识别失败")
        return False


# 从本地加载cookies：
def load_cookies(driver):
    """从本地文件加载cookies"""
    # 要先跳转到登录页面，才能添加cookies，（去到那里才能干某件事）
    driver.get("http://47.107.116.139/fangwei/m.php?m=Public&a=login&")
    try:
        with open("temp/cookies.json") as f:
            cookies = json.loads(f.read())
        for cookie in cookies:
            driver.add_cookie(cookie)
        print("是从本地文件读取的cookies.json")
        driver.refresh()  # 刷新页面，向服务器发送cookie，加入cookie后则第37行的登录会自动跳转不再需要执行输入账号密码验证码等操作
    except:  # 第一次加载页面时没有cookies.json，先pass
        try:
            with open("../temp/cookies.json") as f:
                cookies = json.loads(f.read())
            for cookie in cookies:
                driver.add_cookie(cookie)
            print("是从本地文件读取的cookies.json")
            driver.refresh()  # 刷新页面，向服务器发送cookie，加入cookie后则第37行的登录会自动跳转不再需要执行输入账号密码验证码等操作
        except:
            print("第一次加载页面时没有cookies.json")
            pass


# 保存cookies到本地文件
def save_cookies(driver):
    cookies = driver.get_cookies()  # 获取cookies
    try:
        with open("temp/cookies.json", "w") as f:
            f.write(json.dumps(cookies))  # 保存到cookies.json文件
    except:
        with open("../temp/cookies.json", "w") as f:
            f.write(json.dumps(cookies))  # 保存到cookies.json文件


# 判断是否已经登录过
def is_login(driver):
    if "管理员登录" in driver.title:
        print("需要登录")
        return False  # 注意返回的是状态值False，不是字段值“False”，所以判断时为： is False  不是==Fasle
    else:
        print("已经登录过了")
        return True  # 注意返回的是状态值True，不是字段值“True”，所以判断时为： is True  不是==True
