import unittest
from Function.TestCase.login import Login
from Function.TestCase.addApp import AddApp


# 主功能测试用例装载
class SmokeTest(object):
    # 按测试用例类创建测试用例集
    def create_test_suite(self):
        # 编辑测试套件列表(要执行的测试模块)
        cases = [Login, AddApp]
        suite = unittest.TestSuite()
        for i in cases:
            suite.addTest(unittest.makeSuite(i))
        return suite
