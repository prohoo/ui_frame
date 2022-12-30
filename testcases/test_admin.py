from pathlib import Path

from core.KDT import KeyWord
from core.pages import *


def test_new_deal(admin_driver):
    # 已经处理登录状态

    page1 = AdminIndexPage(admin_driver)
    page2 = page1.to_deal()  # 跳转贷款页面
    page3 = page2.new_deal()

    path = r"temp\22.png"
    upload_path = str(Path(path).absolute())


    data = {
        "name": "加钱啊！",
        "shor_name": "钱钱",
        "username": "aaa",
        "cate": "|--信用认证标",
        "upload_path": upload_path,
        "type": "个人消费",
        "contract": "付息还本合同范本【担保】",
        "tcontract": "付息还本合同范本【担保】",
        "amount": "500000",
        "rate": "11",
        "repay_time": "3",
        "enddate": "31",
        "begin_time": "2022-11-06 18:35:08",
    }
    msg = page3.submit(data)
    assert msg == "添加成功"


def test_new_deal_fail(admin_driver):
    # 已经处理登录状态

    page1 = AdminIndexPage(admin_driver)
    page2 = page1.to_deal()  # 跳转贷款页面
    page3 = page2.new_deal()

    path = r"temp\22.png"
    upload_path = str(Path(path).absolute())

    data = {  # 输入错误参数、不输入参数进行添加
        "name": "加钱啊！",
        "shor_name": "钱钱",
        "username": "",
        "cate": "|--信用认证标",
        "upload_path": upload_path,
        "type": "个人消费",
        "contract": "付息还本合同范本【担保】",
        "tcontract": "付息还本合同范本【担保】",
        "amount": "500000",
        "rate": "11",
        "repay_time": "3",
        "enddate": "31",
        "begin_time": "2022-11-06 18:35:08",
    }
    msg = page3.submit(data)
    assert msg == "添加失败"


def test_new_deal_by_kdt(admin_driver):
    admin_driver.refresh()
    data = {
        "name": "加钱啊！",
        "sort_name": "钱钱",
        "username": "aaa",
        "cate": "|--信用认证标",
        "upload_path": r"temp\22.png",
        "type": "个人消费",
        "contract": "付息还本合同范本【担保】",
        "tcontract": "付息还本合同范本【担保】",
        "amount": "500000",
        "rate": "11",
        "repay_time": "3",
        "enddate": "31",
        "begin_time": "2022-11-06 18:35:08",
    }
    kw = KeyWord(admin_driver)   #实例化KeyWord

    # 1. 进入top_iframe,点击'贷款管理'
    kw.iframe_enter("/html/frameset/frame[1]")
    kw.click("贷款管理;;;LINK_TEXT")
    kw.iframe_exit()

    # 2. 进入left_iframe,点击'全部贷款'
    kw.iframe_enter('//*[@id="menu-frame"]')
    kw.click('全部贷款;;;LINK_TEXT')
    kw.iframe_exit()

    # 3.进入main_farme，一下操作元素均在main_farme
    kw.iframe_enter('//*[@id="main-frame"]')
    # 点击新增贷款按钮
    kw.click('/html/body/div[2]/div[3]/input[1]')
    time.sleep(2)
    # 贷款名称
    kw.input('/html/body/div[2]/form/table[1]/tbody/tr[4]/td[2]/input', data['name'])
    # 简短名称
    kw.input('/html/body/div[2]/form/table[1]/tbody/tr[5]/td[2]/input', data['sort_name'])
    # 会员名称
    kw.input('/html/body/div[2]/form/table[1]/tbody/tr[6]/td[2]/input[1]', data['username'])
    # 会员确认按钮
    kw.click('/html/body/div[5]/ul/li[2]')
    # 选择城市
    kw.click('//*[@id="citys_box"]/div[1]/div[2]/input[1]')
    # 分类
    kw.select('/html/body/div[2]/form/table[1]/tbody/tr[8]/td[2]/select', data['cate'])

    #图片上传 / 本地上传按钮  /文件上传的input框  /确认上传按钮
    kw.click('/html/body/div[2]/form/table[1]/tbody/tr[14]/td[2]/span/div[1]/div/div/button')
    kw.click('//li[text()="本地上传"]')
    kw.upload('//input[@type="file"]', data['upload_path'])
    kw.click('//input[@value="确定"]')

    # 借款用途
    kw.select('/html/body/div[2]/form/table[1]/tbody/tr[15]/td[2]/select', data['type'])
    # 借款合同范本
    kw.select('/html/body/div[2]/form/table[1]/tbody/tr[17]/td[2]/select', data['contract'])
    # 转让合同范本
    kw.select('/html/body/div[2]/form/table[1]/tbody/tr[18]/td[2]/select', data['tcontract'])
    # 借款金额 有
    kw.input('/html/body/div[2]/form/table[1]/tbody/tr[19]/td[2]/input', data['amount'], force=True)
    # 借款利率
    kw.input('/html/body/div[2]/form/table[1]/tbody/tr[27]/td[2]/input', data['rate'], force=True)
    # 借款期限
    kw.input('//*[@id="repay_time"]', data['repay_time'])
    # 筹标期限
    kw.input('/html/body/div[2]/form/table[1]/tbody/tr[28]/td[2]/input', data['enddate'])
    # 借款状态
    kw.click('html/body/div[2]/form/table[1]/tbody/tr[33]/td[2]/label[1]/input')
    # 时间输入框
    kw.input('//*[@id="start_time"]', data['begin_time'], force=True)
    # 提交按钮
    kw.click('/html/body/div[2]/form/table[6]/tbody/tr[2]/td[2]/input[4]')
    time.sleep(2)  #提交了可不能sleep啊

    # 返回信息
    msg =('/html/body/div/table/tbody/tr[3]/td').text

    assert msg == "添加成功"