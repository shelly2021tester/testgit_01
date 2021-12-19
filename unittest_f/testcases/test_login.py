'''
@File:test_login.py
@DateTime:2021/12/16 11:27
@Author:shelly
@Desc:
'''
from pageobject.loginobject import Loginpage
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
import unittest
from config.config import driver_path,url,file,sheet1
from data.readwrite import Read_Write
from BeautifulReport import BeautifulReport


class TestCases(unittest.TestCase):

    def setUp(self):
        print("打开浏览器")
        e = Service(driver_path)
        self.driver = webdriver.Chrome(service=e)
        self.driver.maximize_window()
        self.driver.get(url)
        self.page=Loginpage(self.driver)
        self.doc1=Read_Write(file,sheet1)
        self.data_list = self.doc1.read()

    def tearDown(self):
        print("退出系统")
        self.driver.quit()


    def test_login_success(self):
        '''成功登录'''
        self.page.type_username(self.data_list[0][0])
        self.page.type_password(self.data_list[0][1])
        self.page.click_login()
        sleep(2)
        try:
            assert self.driver.title == "我的地盘 - 禅道"
            print("登录成功")

            self.page.click_logout()
        except:
            print("登录失败")



    def test_login_wrongpassword(self):
        '''错误的密码登录'''
        self.page.type_username(self.data_list[1][0])
        self.page.type_password(self.data_list[1][1])
        self.page.click_login()
        sleep(2)
        alert=self.driver.switch_to.alert
        try:
            assert "登录失败" in alert.text
            print("错误的密码登录失败")
        except:
            print("测试用例失败")

    def test_login_notexistuser(self):
        '''不存在的用户登录'''
        self.page.type_username(self.data_list[2][0])
        self.page.type_password(self.data_list[2][1])
        self.page.click_login()
        sleep(2)
        alert=self.driver.switch_to.alert
        try:
            assert "登录失败" or"次" in alert.text
            print("无效用户登录失败")
        except:
            print("测试用例失败")

if __name__=='__main__':
    # unittest.main()
    suite=unittest.TestSuite()  #定义了一个套件，用来加载测试用例
    suite.addTest(TestCases("test_updateuser"))
    suite.addTest(TestCases("test_adduser"))
    runner=unittest.TextTestRunner()  #定义了一个执行器，用来执行测试用例
    runner.run(suite)