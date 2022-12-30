import logging
import unittest
from pprint import pprint

import allure
import ddt
import pytest
from urllib3 import request

from core.KDT import KeyWord

logger = logging.getLogger(__name__)


def handle_name(s):
    try:
        l = s.index("(")
        r = s.index(")")
        case_name = s[:l]  # 用例名称
        fixture_name = s[l + 1: r]  # 夹具名称
        return case_name, fixture_name
    except:
        logger.error("解析用例名出错", exc_info=True)
        return s, "driver"

def handle_step(s):
    name = s[1]
    key = s[2]
    args = []
    for arg in s[3:]:
        if arg is not None:
            args.append(arg)
    return name, key, args

"""
#使用unittest(本身不能实现数据驱动，其工具ddt能实现)的数据驱动工具ddt，能实现根据所传入的数据 生成测试用例并执行（unittest（python自带unittest）较为方便实现数据驱动）
#ddt: Data-Driven Tests
# 在类前加装饰器【@ddt.ddt】，声明当前类是一个数据驱动测试类，class TestA(unittest.TestCase):为固定写法
# 在方法前加一个装饰器【*@ddt.data(*cases[0]["case_list"])】，固定写法
# 用来指定测试数据源，要求数据源的格式不能是数组或者列表，在数据前加一个星号，相当于是这个数据源里的多个参数
"""

"""创建unitest用例"""


# suite_list：是整个excel表 所有sheet页的数据所有数据
def create_unitest_case(suite_list):
    Test_list = []  # 列表中的测试用例不会被pytest识别
    for case in suite_list:  # 列表中读取每一个工作表，此时case为每一张sheet页的数据
        # print(f'@@!!{case}')
        @ddt.ddt()
        class TestA(unittest.TestCase):  # 创建测试用例
            @ddt.data(*case["case_list"])  # 1.因为是列表，加个* 解包；2.此时的case数据格式中包含了case_list，  17行可打印case信息来看
            def test_unitest_case(self, case):  # 这里一定要test开头
                """
                unittest的ddt中的固定写法，unittest机制会根据所传参数：*case["case_list"]的数据个数（这里是用例条数），自动执行test_exec_cases多少次，
                并补上执行后的后缀test_exec_cases_1、test_exec_cases_2等,传入多少条数据就执行多少次
                """
                # print(case)
                pass

        Test_list.append(TestA)  # 创建好的用例TestA加入到用例列表Test_list
    # print(Test_list)
    return Test_list  # 返回真实可测试的用例，但不是全局变量，还不能被pytest捕获，所以还要创建为全局变量，再让pytest自动捕获到生成的Test_list用例信息并执行


"""创建pytest用例"""


def create_pytest_case(suite_list):
    test_list = []
    for suite in suite_list:
        @allure.feature("Web自动化测试平台")
        @allure.story(suite["name"])
        @pytest.mark.parametrize("case", suite["case_list"],ids=[case["name"] for case in suite["case_list"]], )  # 参数化的名字
        def test_pytest_case(case, request):
            logger.info("测试用例开始执行")
            # print(data)
            # 调用conftest中的浏览器
            # 根据excel内容动态调用指定夹具
            # 1.从excel中拿到用例名称  ： 用例1（admin_driver）
            # 2.从用例名称中解析出夹具名称：  admin_driver
            # case_name = handle_name(case["name"])[0]
            fixture_name = handle_name(case["name"])[1]
            driver = request.getfixturevalue(fixture_name)
            kw = KeyWord(driver)
            for step in case["steps"]:
                name, key, args = handle_step(step)
                logger.info(f"执行关键字{name=}, {key=}, {args=}")
                with allure.step(name):   #在allure报告中显示测试步骤用
                    func = getattr(kw, key)  #通过反射，拿到关键字执行函数
                    func(*args)  #调用关键字函数
                allure.attach(driver.get_screenshot_as_png(), name)
            logger.info("测试用例执行结束")
        test_list.append(test_pytest_case)
    return test_list
