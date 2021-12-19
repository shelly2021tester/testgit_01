'''
@File:atest_bug.py
@DateTime:2021/12/16 11:27
@Author:shelly
@Desc:
'''

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
import unittest
import win32con
import win32gui
from selenium.webdriver.support.select import Select
from config.config import driver_path,url,upload_file

class TestCases(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("打开浏览器")
        e = Service(driver_path)
        cls.driver = webdriver.Chrome(service=e)
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)
        cls.driver.get(url)

    @classmethod
    def tearDownClass(cls):
        print("关闭浏览器")
        cls.driver.quit()

    def setUp(self):
        print("登录系统")
        self.driver.find_element(By.CSS_SELECTOR, "#account").send_keys("pm_2021")
        self.driver.find_element(By.CSS_SELECTOR, "[name=password]").send_keys("p@ssw0rd")
        self.driver.find_element(By.CSS_SELECTOR, "#submit").click()
        sleep(2)

    # def tearDown(self):
    #     print("退出系统")
    #     self.driver.find_element(By.CLASS_NAME, "user-name").click()
    #     self.driver.find_element(By.LINK_TEXT, "退出").click()

    def test_activebug(self):
        '''成功添加激活状态的bug'''
        print("成功添加激活状态的bug")
        self.driver.find_element(By.LINK_TEXT, "Bug").click()
        self.driver.find_element(By.LINK_TEXT, "提Bug").click()
        self.driver.find_element(By.CLASS_NAME, "chosen-choices").click()
        self.driver.find_element(By.CSS_SELECTOR, "li[title*='主干']").click()
        self.driver.find_element(By.ID, "title").send_keys("test")
        js = "var q=document.documentElement.scrollTop=1000"
        self.driver.execute_script(js)
        self.driver.find_element(By.CSS_SELECTOR, ".file-input-empty>button").click()
        sleep(3)
        # FindWindow(class,caption)
        win_first = win32gui.FindWindow("#32770", "打开")
        # FindWindowEx(parent,class,status,caption)
        win_second = win32gui.FindWindowEx(win_first, 0, "ComboBoxEx32", None)
        win_third = win32gui.FindWindowEx(win_second, 0, "ComboBox", None)
        edit = win32gui.FindWindowEx(win_third, 0, "Edit", None)
        button = win32gui.FindWindowEx(win_first, 0, "Button", "打开(&O)")
        win32gui.SendMessage(edit, win32con.WM_SETTEXT, None, upload_file)
        win32gui.SendMessage(win_first, win32con.WM_COMMAND, 1, button)

        sleep(4)
        self.driver.find_element(By.ID, "submit").click()
    def test_resolvedbug(self):
        '''已解决状态的bug'''
        print("已解决状态的bug")
        self.driver.find_element(By.LINK_TEXT,"Bug").click()
        self.driver.find_element(By.CSS_SELECTOR,"a[id=bysearchTab]").click()
        sleep(2)
        self.driver.find_element(By.CSS_SELECTOR,".fieldWidth").click()
        self.driver.find_element(By.CSS_SELECTOR, ".chosen-results :nth-child(7)").click()
        self.driver.find_element(By.CSS_SELECTOR, "#valueBox1").click()
        self.driver.find_element(By.CSS_SELECTOR, "a[title='激活']").click()
        sleep(2)
        self.driver.find_element(By.XPATH,"//tr[@id='searchbox4']/td[2]").click()
        sleep(2)
        self.driver.find_element(By.CSS_SELECTOR,"div[id='field4_chosen'] [title='是否确认']").click()
        # self.driver.find_element(By.XPATH, "//td[@class='w-400px']/table/tbody/tr[1]/td[4]").click()
        elem=self.driver.find_element(By.ID,"value4")
        Select(elem).select_by_value("ZERO")
        self.driver.find_element(By.ID,"submit").click()
        sleep(2)
        self.driver.find_element(By.XPATH,"//table[@id='bugList']/tbody/tr[1]/td[11]/a[1]").click()
        sleep(5)
        self.driver.switch_to.frame("iframe-triggerModal")
        self.driver.find_element(By.ID,"submit").click()
        sleep(5)



if __name__=='__main__':
    # unittest.main()
    suite=unittest.TestSuite()  #定义了一个套件，用来加载测试用例
    suite.addTest(TestCases("test_resolvedbug"))
    # suite.addTest(TestCases("test_adduser"))
    runner=unittest.TextTestRunner()  #定义了一个执行器，用来执行测试用例
    runner.run(suite)