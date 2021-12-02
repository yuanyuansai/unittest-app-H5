# -*- coding: cp936 -*-
#coding = utf-8

import unittest, time, re
from util import HTMLTestRunner
import os
from util.send_email import sendEmail
class RunTest:
    def go_on_run(self):
        #����creatsuite������������Ҫ��ӵ�test*.py�ļ���ɵĲ����׼�
        now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        report = os.path.join(os.getcwd(), "report\\")
        filename = report + now + 'result.html'
        print(filename)
        suite=unittest.TestSuite()
        loader=unittest.TestLoader()
        suite.addTest(loader.discover(os.path.join(os.getcwd(), "test_case\\")))

        runner = HTMLTestRunner.HTMLTestRunner(stream=open(filename, "wb"),  # ��һ�������ļ������������stream
                                description="",  # ��������ʾ��������Ϣ
                                title="�ӿڲ��Ա���")  # ����ı���

        # ʹ��������ȥִ�в����׼��������
        runner.run(suite)
        sendEmail.sendmain(filename)

if __name__ == '__main__':
    run=RunTest()
    run.go_on_run()



