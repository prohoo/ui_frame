import time
from pathlib import Path

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class KeyWord:
    _split_char = ";;;"  # 作为分割用例表达式的标记，以;;;进行分割

    def __init__(self, driver: Chrome):  # 在参数中加入：是对参数的预解析，可以提示该参数为什么数据类型补全等
        """
        实例化后的默认参数及特性
        :param driver: Chrome或火狐等
        """
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)  # 最多等10秒

    def get(self, url):
        """
        跳转到指定页面
        :param url:
        :return:
        """
        self.driver.get(url)

    def find_element(self, loc_expre: str):
        """
        元素定位
        1.自动等待元素出现
        2.对定位参数进行二次处理
        :param loc_expre: 元素的定位表达式，格式“value;;;by”  ，所以传表达式时，如果不用默认的xpath，则需加上;;;和表达式
        :return: element
        """
        value, *by = loc_expre.split(self._split_char)  # 从字符串中截取定位策略
        if not by:
            by = By.XPATH  # 如果没有指定定位策略，默认使用Xpath
        else:
            by = getattr(By, by[0])  # 反射源码by.py中的类By中的属性by[0]，by[0]是截取到的定位策略，如ID、LINK_TEXT等
            # 这反射用意就是，填了什么XPATH，它会去by.py里找并反射该属性给你

        def f(driver):
            return self.driver.find_element(by, value)

        element = self.wait.until(f)
        return element

    def click(self, loc_expre, force=False):
        """
        点击元素 ,支持强制点击
        :param loc_expre :定位表达式
        :param force :默认不强制点击
        :return:
        """
        element = self.find_element(loc_expre)
        if force:
            self.driver.execute_script("arguments[0].click()", element)  # 通过js脚本强制点击
        else:
            element.click()  # 普通点击

    def sleep(self, second):
        time.sleep(second)

    def input(self, loc_expre, value, force=False):
        """
        注意参数顺序要一致
        输入内容，支持强制输入
        :param value:
        :param loc_expre :元素定位表达式
        :param force: 是否强制输入，有些元素如日期表输入，不好输入，就需要强制输入
        :return:
        """
        element = self.find_element(loc_expre)
        if force:
            self.driver.execute_script(f"arguments[0].value='{value}'", element)
        else:
            element.send_keys(value)

    def clear(self, loc_expre, force=False):
        """
        清空元素
        :param loc_expre: 元素定位表达式
        :param force: 是否强制清空
        :return:
        """
        element = self.find_element(loc_expre)
        if force:
            self.driver.execute_script("arguments[0].value=''", element)
        else:
            element.clear()

    def iframe_enter(self, loc_expre):
        """
        进入指定iframe
        :param loc_expre: 元素定位表达式
        :return:
        """
        element = self.find_element(loc_expre)
        self.driver.switch_to.frame(element)

    def iframe_exit(self):
        """
        退出iframe
        :return:
        """
        self.driver.switch_to.default_content()

    def select(self, loc_expre, text):
        """

        :param loc_expre: 元素定位表达式
        :param text: 所选择的文本
        :return:
        """
        element = self.find_element(loc_expre)
        Select(element).select_by_visible_text(text)

    def upload(self, loc_expre, file):
        """
        输入文件路径式的上传
        :param loc_expre: 元素定位表达式
        :param file: 文件路径
        :return:
        """
        element = self.find_element(loc_expre)
        # Path()可以将file路径（相对、绝对路径都可以）转变成path对象，然后path对象就能使用absolute()
        path = Path(file).absolute()  # 把该路径对象转换成 绝对路径
        element.send_keys(str(path))

    def assert_text(self, loc, text):
        """
        断言：文本断言
        :param loc: 元素定位表达式
        :param text: 所断言文本
        :return:
        """
        element = self.find_element(loc)
        assert element.text == text
