import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from core.funcs import img2code, save_cookies, load_cookies, is_login

driver = webdriver.Chrome()
driver.implicitly_wait(5)  #隐式等待

load_cookies(driver)  #浏览器启动后，加载cookies


#1.先启动浏览器；2再加载cookies，有则在load_cookies已登录；
# 无则代表没登录过==》去登录==》3.判断是否已经登录过（没有登录过则进行登录，登录完后执行保存cookie操作）

#进入登录首页


#判断：如果未登录，则需要走登录流程
if is_login(driver) is False:
    driver.get("http://47.107.116.139/fangwei/m.php?m=Public&a=login&")
    print(driver.title)
    # 对验证码元素进行截图定位
    driver.find_element(By.XPATH, '//*[@id="verify"]').screenshot("verify.png")
    code = img2code("verify.png")  # 识别验证码
    if code:  #识别成功
        driver.find_element(By.XPATH, "/html/body/form/table/tbody/tr/td[3]/table/tbody/tr[2]/td[2]/input").send_keys(
            "admin")
        driver.find_element(By.XPATH, "/html/body/form/table/tbody/tr/td[3]/table/tbody/tr[3]/td[2]/input").send_keys(
            "msjy123")
        driver.find_element(By.XPATH, "/html/body/form/table/tbody/tr/td[3]/table/tbody/tr[5]/td[2]/input").send_keys(
            code)
        driver.find_element(By.XPATH, '//*[@id="login_btn"]').click()
    else:
        print("识别验证码失败，无法登录")


#在元素的上一行debug
# debugger(driver) #debugger模式下，selenium定位不到,
# 浏览器（F12==》consolo==》$x('XPATH路径')）可以定位到，首先考虑遇到了frame元素（目的是前端模块化，一般是老项目会有）
#F12 Elment可以看到多个 frame ui框架，每个frame里都是一个独立的网页 ，网页嵌套网页，
# frame里的网页内容其实不在当前网页，所以想进入frame网页，则先进入frame框架frame

#先定位到frame ui框架

# debugger(driver)
top_frame = driver.find_element(By.XPATH,'/html/frameset/frame[1]')
driver.switch_to.frame(top_frame)  #切换到顶部frame
#打开新增贷款页面
driver.find_element(By.XPATH,'//*[@id="navs"]/ul/li[2]/a').click()  #贷款管理
driver.switch_to.default_content()  #进入指定frame后要回退到默认的注frame，不然会一直在指定frame找元素，则定位不到别的frame

menu_frame = driver.find_element(By.XPATH,'//*[@id="menu-frame"]')
driver.switch_to.frame(menu_frame)
driver.find_element(By.XPATH,'/html/body/dl[1]/dd[1]/a').click()  #全部贷款
driver.switch_to.default_content()

main_frame = driver.find_element(By.XPATH,'//*[@id="main-frame"]')
driver.switch_to.frame(main_frame)
driver.find_element(By.XPATH,'/html/body/div[2]/div[3]/input[1]').click() #新增贷款


#贷款名称
driver.find_element(By.XPATH,'/html/body/div[2]/form/table[1]/tbody/tr[4]/td[2]/input').send_keys('求富婆包养！')
#简短名称
driver.find_element(By.XPATH,'/html/body/div[2]/form/table[1]/tbody/tr[5]/td[2]/input').send_keys('简短名称')
#会员名称
driver.find_element(By.XPATH,'/html/body/div[2]/form/table[1]/tbody/tr[6]/td[2]/input[1]').send_keys('aaa')
time.sleep(1)
driver.find_element(By.XPATH,'/html/body/div[5]/ul/li[2]').click()
#选择分类
el = driver.find_element(By.XPATH,'/html/body/div[2]/form/table[1]/tbody/tr[8]/td[2]/select')  #选择框不需要.click()
#下拉选择框的三种选择方式，前提：1.前端用了<Select>标签，2.先定位到下拉框
# Select(el).select_by_visible_text('|--信用认证标')  #一般用可视文本定位
Select(el).select_by_index(1)
# Select(el).select_by_value('3')

#借款合同范本
el = driver.find_element(By.XPATH,'/html/body/div[2]/form/table[1]/tbody/tr[17]/td[2]/select')
Select(el).select_by_visible_text("等额本息合同范本【担保】")
#转让合同范本
el = driver.find_element(By.XPATH,'/html/body/div[2]/form/table[1]/tbody/tr[18]/td[2]/select')
Select(el).select_by_visible_text("等额本息合同范本【担保】")
#贷款金额
el = driver.find_element(By.XPATH,'/html/body/div[2]/form/table[1]/tbody/tr[19]/td[2]/input')
el.clear()
el.send_keys('50000')  #注意输入字符串
#年利率
driver.find_element(By.XPATH,'/html/body/div[2]/form/table[1]/tbody/tr[27]/td[2]/input').send_keys('5')

#借款期限
driver.find_element(By.XPATH,'//*[@id="repay_time"]').send_keys('3')
#筹标期限
driver.find_element(By.XPATH,'/html/body/div[2]/form/table[1]/tbody/tr[28]/td[2]/input').send_keys('30')
#借款用途
el = driver.find_element(By.XPATH,'/html/body/div[2]/form/table[1]/tbody/tr[15]/td[2]/select')
Select(el).select_by_visible_text("个人消费")


#上传图片按钮
driver.find_element(By.XPATH,'/html/body/div[2]/form/table[1]/tbody/tr[14]/td[2]/span/div[1]/div/div/button').click()


#点击“本地上传”按钮  #这里的按钮XPATH会一直变化，所以得手写XPATH
driver.find_element(By.XPATH,'//li[text()="本地上传"]').click()
#点击浏览按钮，这里的浏览按钮被别的元素遮蔽了，需要在F12控制台 ,通过$x('')找到type=file的input框的XPATH，不是type=button的
#文件上传的input框不能点击（否则需要人为操作选择文件），则通过send_keys()输入文件路径
el = driver.find_element(By.XPATH,'//input[@type="file"]')
#文件input框上传文件：
el.send_keys(r"C:\Users\hl\Desktop\pytest相关\ui_frame\pp.png")  #输入文件的 绝对 路径
#点击确认上传按钮
driver.find_element(By.XPATH,'//input[@value="确定"]').click()

#选择所在城市  复选框checkbox ，可以选多个的为复选框，只能选单个的为单选框
driver.find_element(By.XPATH,'//*[@id="citys_box"]/div[1]/div[2]/input[1]').click()
#借款状态
driver.find_element(By.XPATH,'/html/body/div[2]/form/table[1]/tbody/tr[33]/td[2]/label[1]/input').click()

#日期时间选择框：难定位，直接对输入框输入日期即可，如果不能通过send_keys输入，则通过执行js脚本强制输入

el = driver.find_element(By.XPATH,'//*[@id="start_time"]')
#输入前，改el不在可视范围，需要先把el滚动到可视范围
driver.execute_script("arguments[0].scrollIntoView()",el)  #让元素显示出来后，才能进行输入操作
driver.execute_script("arguments[0].value='2022-11-06 18:35:08'",el)


# debugger(driver)  #debugger调试时，可以输入c让程序继续运行
#新增按钮
driver.find_element(By.XPATH,'/html/body/div[2]/form/table[6]/tbody/tr[2]/td[2]/input[4]').click()


#返回列表



save_cookies(driver)  #浏览器关闭前保存cookies


# input()
driver.quit()





