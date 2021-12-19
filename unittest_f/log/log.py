'''
@File:log.py
@DateTime:2021/9/28 15:15
@Author:shelly
@Desc:None
'''
import logging

logger=logging.getLogger()
logger.setLevel(logging.INFO)
format=logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
logFile=r'E:\online_learning\module1\B_web_selenium\selenium_day7\unittest_f\log\log.txt'
fh = logging.FileHandler(logFile, mode='a', encoding='utf-8')
fh.setLevel(logging.INFO)
fh.setFormatter(format)
logger.addHandler(fh)