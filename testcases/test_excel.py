from pprint import pprint

from core.read_excel_data import load_case_by_excel
from core.createCase import *

suite_list = load_case_by_excel("testcases/testcases.xlsx")   #加载excel数据
# pprint(suite_list)
test_list = create_pytest_case(suite_list)    #根据加载到的数据，

# 创建pytest可以自动识别并执行的用例：

"""--------------start----------------------生成unitest用例-----------------------start"""
#所生成的Test_list不能被pytest识别， 不能用pytest .\test_excel.py -vs  (-vs：显示参数)运行，保存为全局变量即可运行,
#下面把用例数据设置为全局参数，让pytest自动识别到并执行？？？
# i = 0
# for test in Test_list:
#     #循环时本身会创建test、test_1、test_2： 作为unitest.TestCase的子类，test为循环出的一个多余的类变量：test本身，需要干掉：test = None
#     i = i+1
#     print(f'@@{test}')
#     globals()[f'test_{i}'] = test   #循环生成的Test开头的函数（用例），让pytest框架识别到并执行生成的函数（用例），如Test、Test_1、Test_2三个全局变量
# test = None  #test不再是 unitest.TestCase的子类，不能让Test重复执行，只能执行test_1、test_2
"""--------------end------------------------生成unitest用例-----------------------end"""

i = 0
for a in test_list:
   #改成atest后，就不会生成test本身而是atest，用例就少了本身的test，则不需要再test = None干掉
    i = i+1
    globals()[f'test_{i}'] = a
    print(a)

# pprint(suite_list)
# print(Test_list)
# print(len(Test_list))