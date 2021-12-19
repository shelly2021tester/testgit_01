'''
@File:runner.py
@DateTime:2021/12/16 11:28
@Author:shelly
@Desc:
'''

import unittest
from BeautifulReport import BeautifulReport
from config.config import case_dir,report_path

#获取测试用例
cases=unittest.defaultTestLoader.discover(start_dir=case_dir,pattern='test*.py')
#执行测试用例
result= BeautifulReport(cases)
#生成测试报告
result.report(description="登录和注册的测试报告",filename="SIT测试报告",report_dir=report_path)