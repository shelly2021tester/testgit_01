'''
@File:loginobject.py
@DateTime:2021/12/17 11:17
@Author:shelly
@Desc:
'''
from selenium.webdriver.common.by import By

class Loginpage:
    def __init__(self,driver):
        self.account=By.CSS_SELECTOR,"#account"
        self.password=By.CSS_SELECTOR,"[name=password]"
        self.button=By.CSS_SELECTOR,"#submit"
        self.driver=driver
        self.user=By.CLASS_NAME,"user-name"
        self.buttonlogout=By.LINK_TEXT,"退出"

    def type_username(self,username):
        self.driver.find_element(*self.account).send_keys(username)

    def type_password(self,password):
        self.driver.find_element(*self.password).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.button).click()

    def click_logout(self):
        self.driver.find_element(*self.user).click()
        self.driver.find_element(*self.buttonlogout).click()


