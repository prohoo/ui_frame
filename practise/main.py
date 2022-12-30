import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

#启动浏览器方式一：
from selenium import webdriver
driver = webdriver.Chrome()  #启动浏览器
driver.fin
#启动浏览器方式二：
# from webdriver_helper.driver import get_webdriver
# driver = get_webdriver()  # #启动浏览器

#登录进入页面
#driver.get("http://baidu.com")

#获取WebElement对象
    #方法一：
# l = driver.find_elements(By.XPATH,'//*[@id="s-top-left"]/a')
#
# # for i in l:
# #     print(i.text)
# if l:
#     print("定位成功")
# else:
#     print("定位失败")
    #方法二driver.find_element(By.XPATH,'//*[@id="s-top-left"]/a')

# -start----------------------------------------------webelement的属性----------------------start--
# -start----------------------------------------------webelement的属性-----------------------start--

# driver.implicitly_wait(5)
# driver.get("http://baidu.com")  #对浏览器进行操作控制
# el = driver.find_element(By.XPATH,'//*[@id="s22-top-left"]/a')
# print("隐式等待")
#
# el = driver.find_element(By.LINK_TEXT,"新闻")
# print(el.text)
# el2 = driver.find_element(By.XPATH,'//*[@id="su"]')
# el3 = driver.find_element(By.CSS_SELECTOR,"#su")
# el = driver.find_element(By.ID,"kw")
# print(el.id)  #唯一标记
# print(el.tag_name)  #标签名
# print(el.text)
# print(el.location)  #元素坐标
# print(el.size)  #大小
# print(el.rect)  #范围
# print(el.parent)  #WebDriver实例
# # print(el.screenshot_as_base64)
# driver.get_screenshot_as_file('./c.png')  #driver获取全屏截图

# driver.find_element(By.XPATH,'//*[@id="verify"]').screenshot("verify.png")
# open("d.png","wb").write(el.screenshot_as_png)  #webelement保存当前对象的截图

#
# print(el.get_attribute("autocomplete"))  #获取元素的HTML属性 如：input框里的id、name、class、value等值
# el.get_attribute("id")
# el.get_attribute("value")
# -end------------------------------------------------webelement的属性----------------end--
# -end------------------------------------------------webelement的属性-----------------end--

# -start----------------------------------------------webelement的元素操作-------------start--
# -start----------------------------------------------webelement的元素操作-------------start--
# el.click()
# el.send_keys("aaa")
# el.clear()
# -end------------------------------------------------webelement的元素操作-------------end--
# -end------------------------------------------------webelement的元素操作-------------end--
# el.send_keys("321321")

# -start------------------------------------------------webelement的键鼠操作-------------start--
# -start------------------------------------------------webelement的键鼠操作-------------start--
#########键盘
# 1.功能：F1~F12
# 2.字母键：A~Z
# 3.数字键：0~9
# 4.编辑键：Home、End、。。。
# 5.方向键：上下左右
# 特殊的键，Selenium提供常量from selenium.webdriver.common.keys  import keys
# from selenium.webdriver.common.keys import Keys
# ac = ActionChains(driver)  #实例化ac
# ac.key_down(Keys.CONTROL)  #摁下  control键  抬起：ac.key_down(Key.CONTROL) ,注意K为大写
# ac.send_keys("a")  #输入keys  “a”
# ac.perform()  #执行actions，必须要执行


################
# 鼠标
# 移动：
#移动到指定的坐标：move_by_offset(??)
#移动到指定的元素：move_by_element(el)

# 左键点击ac.click()、右键点击：ac.context_click()

# -end------------------------------------------------webelement的键鼠操作-------------end--
# -end------------------------------------------------webelement的键鼠操作-------------end--



# driver.maximize_window()
# driver.back()
# driver.forward()
# driver.refresh()
# # driver.set_window_size(1000,200)
# print(driver.current_url)
# html = driver.page_source
# #
# if html.count("百度一下")>=1:
#     print("这是百度")
# print(driver.title)
# content = driver.get_screenshot_as_png()
# with open("b.png","wb") as f:
#     f.write(content)
#
# driver.get_screenshot_as_file("./a.png")
#
# el = driver.find_element(By.ID,"su")
# el.get_attribute()
# print(el,type(el))

# driver.quit()


