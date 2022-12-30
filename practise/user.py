import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()

driver.get('http://47.107.116.139/fangwei/index.php')
driver.find_element(By.XPATH,'/html/body/div[2]/div/div[2]/div[1]/div/a').click()
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="login-email-address"]').send_keys('admin')

driver.find_element(By.XPATH,'//*[@id="login-password"]').send_keys('msjy123')
driver.find_element(By.XPATH,'//*[@id="ajax_login_form"]/div/ul/li[3]/label').click()
driver.find_element(By.XPATH,'//*[@id="ajax-login-submit"]').click()
#登录成功弹框的text
# msg = driver.find_element(By.XPATH,'//*[@id="fanwe_success_box"]/table/tbody/tr/td[2]/div[2]').text
# print("登录成功的text：{}".format(msg))
#点击登录成功后的确认按钮
# driver.find_element(By.XPATH,'//input[@value="确定"]').click()

time.sleep(1)
driver.get('http://47.107.116.139/fangwei/index.php?ctl=deal&id=21629')
el = driver.find_element(By.XPATH,'//*[@id="J_BIDMONEY"]')
el.clear()
el.send_keys('40000')
#点击立即投资
driver.find_element(By.XPATH,'//*[@id="tz_link"]').click()
#点击投资后弹框、输入支付密码
time.sleep(10)
driver.find_element(By.XPATH,'//input[@type="password"]').send_keys('msjy123')
driver.find_element(By.XPATH,'//*[@id="J_bindpassword_btn"]').click()

#弹框投标成功，获取text后，点击确定按钮
#显式等待
success_text = WebDriverWait(driver, 10).until(
    lambda x: driver.find_element(By.XPATH,'//*[@id="fanwe_success_box"]/table/tbody/tr/td[2]/div[2]').text)

print("投标成功text："f'{success_text}')
driver.find_element(By.XPATH,'//*[@id="fanwe_success_box"]/table/tbody/tr/td[2]/div[3]/input[1]').click()

