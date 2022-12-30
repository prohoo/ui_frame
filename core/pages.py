import time


from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
# from webdriver_helper import debugger,get_webdriver
from selenium import webdriver
from core.funcs import img2code, is_login


class BasePage:
    """抽象化类，包含所有页面公用代码"""
    def __init__(self, driver: Chrome):
        self.driver = driver  #供下面调用driver使用,此处的driver已在conftest中声明

#不需要声明driver的原因是conftest里已经声明了driver = get_webdriver()，driver其作用域是module

class IndexPage(BasePage):
    '''前台登录页'''
     ##xpath
    xpath_login_link = (By.XPATH,'//*[@id="user_head_tip"]/a[1]')
    xpath_username = (By.XPATH,'//*[@id="login-email-address"]')
    xpath_password = (By.XPATH,'//*[@id="login-password"]')
    xpath_login_btn = (By.XPATH,'//*[@id="ajax-login-submit"]')
    login_result_msg = (By.XPATH,'//div[@class="dialog-content"]')
    ##elements
    def login(self,username,password):
        self.driver.find_element(*self.xpath_login_link).click()
        self.driver.find_element(*self.xpath_username).send_keys(username)
        self.driver.find_element(*self.xpath_password).send_keys(password)
        self.driver.find_element(*self.xpath_login_btn).click()
        time.sleep(1)  ##他妈的有弹框的全部强制等待1-5秒试试艹
        ##显式等待  等到弹框出现再获取,,
        ##一定要注意等待时的判断条件，数据驱动中，反例数据一般不能成立该条件，会导致反例全false

        # debugger(self.driver)
        WebDriverWait(self.driver, 5).until(
            lambda x: "忘记密码？" not in self.driver.find_elements(*self.login_result_msg)[-1].text   #[-1]：取最后一位
            and self.driver.find_elements(*self.login_result_msg)[-1].text != ""
        )
        el_loginSuccss_msg = self.driver.find_elements(*self.login_result_msg)[-1].text
        return el_loginSuccss_msg

class DealPage(BasePage):
    """投资支付"""
    xpath_money = (By.XPATH,'//*[@id="J_BIDMONEY"]')
    xpath_pay_btn = (By.XPATH,'//*[@id="tz_link"]')
    xpath_pay_wait = (By.XPATH,'//*[@id="paypass-box"]/table/tbody/tr/td[2]/div[1]/div[1]')
    xpath_pay_password = (By.XPATH,'//*[@id="J_bid_password"]')
    xpath_comfirm = (By.XPATH,'//*[@id="J_bindpassword_btn"]')

    def pay(self,money,password):
        self.driver.find_element(*self.xpath_money).send_keys(money)
        self.driver.find_element(*self.xpath_pay_btn).click()
        time.sleep(2)
        # WebDriverWait(self.driver,10).until(lambda x: "支付密码" in self.driver.find_element(*self.xpath_pay_wait).text)
        self.driver.find_element(*self.xpath_pay_password).send_keys(password)
        self.driver.find_element(*self.xpath_comfirm).click()
        pay_success_text = WebDriverWait(self.driver, 5).until(
            lambda x: self.driver.find_element(By.XPATH, '//*[@id="fanwe_success_box"]/table/tbody/tr/td[2]/div[2]').text)
        return pay_success_text

class AdminLoginPage(BasePage):
    """后台登录页面"""
    ipt_username = (By.XPATH, '/html/body/form/table/tbody/tr/td[3]/table/tbody/tr[2]/td[2]/input')
    ipt_password = (By.XPATH, '/html/body/form/table/tbody/tr/td[3]/table/tbody/tr[3]/td[2]/input')
    ipt_verify = (By.XPATH, '/html/body/form/table/tbody/tr/td[3]/table/tbody/tr[5]/td[2]/input')
    img_verify = (By.XPATH, '//*[@id="verify"]')
    btn_submit = (By.XPATH, '//*[@id="login_btn"]')

    def login(self,username,password):
        self.driver.find_element(*self.img_verify).screenshot("temp/verify.png")
        time.sleep(2)
        code = img2code("temp/verify.png")  #调用验证码

        self.driver.find_element(*self.ipt_username).send_keys(username)
        self.driver.find_element(*self.ipt_password).send_keys(password)
        self.driver.find_element(*self.ipt_verify).send_keys(code)
        self.driver.find_element(*self.btn_submit).click()  #点击登录后一般存在等待过程
        time.sleep(5)   #等待时间一定要足够，否则还不够跳转到登录首页
        return is_login(self.driver)

class AdminIndexPage(BasePage):
    """后台首页"""

    #如果一个页面中，元素是不断变化的，不用定义属性，只封装框架,常见的会变化：菜单栏点击后生成新的元素，切换页面后页面内容变化？，不会变化：顶部的菜单等

    ifm_top = (By.XPATH, '/html/frameset/frame[1]')
    ifm_left = (By.XPATH, '//*[@id="menu-frame"]')
    ifm_main = (By.XPATH,'//*[@id="main-frame"]')
    """进入贷款页面"""
    def to_deal(self):
        self.driver.refresh()  #要注意，进入页面后要刷新，确保页面回到最初的首页
        #先点击顶部的iframe，点击‘贷款管理’，像菜单栏的文字一般是唯一的a标签，所以最好用LINK_TEXT定位
        top_iframe = self.driver.find_element(*self.ifm_top)
        self.driver.switch_to.frame(top_iframe)  #进入框架
        self.driver.find_element(By.LINK_TEXT,'贷款管理').click()
        self.driver.switch_to.default_content()  #退出框架
        #再点击进入左边的iframe，点击‘全部贷款’
        left_iframe = self.driver.find_element(*self.ifm_left)
        self.driver.switch_to.frame(left_iframe)
        self.driver.find_element(By.LINK_TEXT,'全部贷款').click()
        self.driver.switch_to.default_content()  #退出默认iframe
        main_frame = self.driver.find_element(*self.ifm_main)
        self.driver.switch_to.frame(main_frame)
        #干完这个步骤后，后置条件：要返还到下一个步骤的页面
        time.sleep(1)
        return AdminDealPage(self.driver)   #返回一个新的po

class AdminDealPage(BasePage):
    """贷款管理页"""
    btn_new_deal = (By.XPATH,'/html/body/div[2]/div[3]/input[1]')  #新增贷款的按钮
    tr_deal = (By.XPATH,'//tr[contains(@class,"row")]')
    def new_deal(self):
        time.sleep(1)
        self.driver.find_element(*self.btn_new_deal).click()
        return AdminNewDealPage(self.driver)

class AdminNewDealPage(BasePage):
    """后台-新增贷款页"""
    ipt_name = (By.XPATH, '/html/body/div[2]/form/table[1]/tbody/tr[4]/td[2]/input')  #贷款名称
    ipt_shor_name = (By.XPATH, '/html/body/div[2]/form/table[1]/tbody/tr[5]/td[2]/input')  #简短名称
    ipt_username = (By.XPATH, '/html/body/div[2]/form/table[1]/tbody/tr[6]/td[2]/input[1]')  #会员名称
    btn_username =(By.XPATH, '/html/body/div[5]/ul/li[2]')  #会员确认按钮
    btn_city = (By.XPATH, '//*[@id="citys_box"]/div[1]/div[2]/input[1]')  #选择城市
    sel_cate = (By.XPATH, '/html/body/div[2]/form/table[1]/tbody/tr[8]/td[2]/select')  #分类

    #图片上传
    btn_show_upload = (By.XPATH, '/html/body/div[2]/form/table[1]/tbody/tr[14]/td[2]/span/div[1]/div/div/button')  #图片上传按钮
    btn_show_local_upload = (By.XPATH, '//li[text()="本地上传"]')  #本地上传按钮
    ipt_upload = (By.XPATH, '//input[@type="file"]')  #文件上传的input框
    ipt_submit_upload = (By.XPATH, '//input[@value="确定"]')  #确认上传按钮

    sel_usetype = (By.XPATH,'/html/body/div[2]/form/table[1]/tbody/tr[15]/td[2]/select')  #借款用途
    sel_contract = (By.XPATH,'/html/body/div[2]/form/table[1]/tbody/tr[17]/td[2]/select')  #借款合同范本
    sel_tcontract = (By.XPATH,'/html/body/div[2]/form/table[1]/tbody/tr[18]/td[2]/select')  #转让合同范本
    ipt_amount = (By.XPATH,'/html/body/div[2]/form/table[1]/tbody/tr[19]/td[2]/input')  #借款金额
    ipt_rate = (By.XPATH,'/html/body/div[2]/form/table[1]/tbody/tr[27]/td[2]/input')  #借款利率
    ipt_repay_time = (By.XPATH,'//*[@id="repay_time"]')  #借款期限
    ipt_enddate = (By.XPATH,'/html/body/div[2]/form/table[1]/tbody/tr[28]/td[2]/input')  #筹标期限
    ipt_status = (By.XPATH,'/html/body/div[2]/form/table[1]/tbody/tr[33]/td[2]/label[1]/input')  #借款状态
    ipt_start_time = (By.XPATH,'//*[@id="start_time"]')  #时间输入框
    btn_submit = (By.XPATH,'/html/body/div[2]/form/table[6]/tbody/tr[2]/td[2]/input[4]')  #提交按钮
    msg = (By.XPATH,'/html/body/div/table/tbody/tr[3]/td')  #返回信息

    def submit(self,data):
        """提交新的贷款信息"""
        self.driver.find_element(*self.ipt_name).send_keys(data['name'])
        self.driver.find_element(*self.ipt_shor_name).send_keys(data['shor_name'])
        self.driver.find_element(*self.ipt_username).send_keys(data['username'])
        time.sleep(1)
        # debugger(self.driver)
        self.driver.find_element(*self.btn_username).click()
        self.driver.find_element(*self.btn_city).click()
        el_cate = self.driver.find_element(*self.sel_cate)
        Select(el_cate).select_by_visible_text(data['cate'])  #分类
        #图片上传
        self.driver.find_element(*self.btn_show_upload).click()
        self.driver.find_element(*self.btn_show_local_upload).click()
        self.driver.find_element(*self.ipt_upload).send_keys(data['upload_path'])
        self.driver.find_element(*self.ipt_submit_upload).click()
        #借款用途
        el = self.driver.find_element(*self.sel_usetype)
        Select(el).select_by_visible_text(data['type'])
        #借款合同范本
        el = self.driver.find_element(*self.sel_contract)
        Select(el).select_by_visible_text(data['contract'])
        #转让合同范本
        el = self.driver.find_element(*self.sel_tcontract)
        Select(el).select_by_visible_text(data['tcontract'])
        #借款金额
        el = self.driver.find_element(*self.ipt_amount)
        el.clear()
        el.send_keys(data['amount'])
        #借款利率
        el = self.driver.find_element(*self.ipt_rate)
        el.clear()
        el.send_keys(data['rate'])
        # 借款/还款期限
        el = self.driver.find_element(*self.ipt_repay_time)
        el.clear()
        el.send_keys(data['repay_time'])
        # 筹标期限
        el = self.driver.find_element(*self.ipt_enddate)
        el.clear()
        el.send_keys(data['enddate'])
        #借款状态
        self.driver.find_element(*self.ipt_status).click()
        # 时间输入框
        el = self.driver.find_element(*self.ipt_start_time)
        self.driver.execute_script("arguments[0].scrollIntoView()", el)
        self.driver.execute_script(f"arguments[0].value='{data['begin_time']}'", el)
        #提交按钮
        self.driver.find_element(*self.btn_submit).click()

        #返回系统提示
        el = self.driver.find_element(*self.msg)
        return el.text




if __name__ == "__main__":

    """单页面调试用"""
    # driver = get_webdriver()
    # driver.maximize_window()
    # driver.implicitly_wait(3)
    #
    # driver.get("http://47.107.116.139/fangwei/index.php")
    # page = IndexPage(driver)  #实例化一个page  pom对象
    # msg = page.login("admin","msjy123")
    # print(msg+"??????????")
#
#     driver.get('http://47.107.116.139/fangwei/index.php?ctl=deal&id=21688')
#     page = DealPage(driver)
#     pay_msg = page.pay('100','msjy123')
#     print(pay_msg)
