# -*- coding: cp936 -*-
#coding = utf-8

import unittest, time, re
from util import HTMLTestRunner
import os
from util.send_email import sendEmail
class RunTest:
    def go_on_run(self):
        #调用creatsuite方法，返回需要添加的test*.py文件组成的测试套件
        now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        report = os.path.join(os.getcwd(), "report\\")
        filename = report + now + 'result.html'
        print(filename)
        suite=unittest.TestSuite()
        loader=unittest.TestLoader()
        suite.addTest(loader.discover(os.path.join(os.getcwd(), "test_case\\")))

        runner = HTMLTestRunner.HTMLTestRunner(stream=open(filename, "wb"),  # 打开一个报告文件，将句柄传给stream
                                description="",  # 报告中显示的描述信息
                                title="接口测试报告")  # 报告的标题

        # 使用启动器去执行测试套件里的用例
        runner.run(suite)
        sendEmail.sendmain(filename)

if __name__ == '__main__':
    run=RunTest()
    run.go_on_run()



