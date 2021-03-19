import unittest
from HTMLTestRunnerNew import HTMLTestRunner
from tools.get_path import *
from tools import test_usedCar
from tools.login_getCookies import login
s=login()
suite=unittest.TestSuite()
loader=unittest.TestLoader()
suite.addTest(loader.loadTestsFromModule(test_usedCar))

with open(test_report_path,'wb') as file:
    runner=HTMLTestRunner(stream=file, verbosity=2,tester='李晓良',title='接口自动化测试报告',description=None)
    runner.run(suite)










































loader=unittest.TestLoader()
suite.addTest(loader.loadTestsFromModule(test_usedCar))


with open(test_report_path,'wb') as file:
    runner=HTMLTestRunner(stream=file, verbosity=2,tester='李晓良',title='接口自动化测试报告',description=None)
    runner.run(suite)