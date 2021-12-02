# -*- coding: cp936 -*-
#coding = utf-8

import unittest, time, re
import HTMLTestRunner,os
import xlrd
import sys
#reload(sys)
#sys.setdefaultencoding('utf8')


def creatsuite():

    #1---�ҵ����е�test*py�ļ�
    testunit = unittest.TestSuite()
    #��������ļ�����Ŀ¼
    # test_dir = os.path.join(os.getcwd(), "test_case")
    test_dir = r"D:\BaiduNetdiskDownload\����\unittest\test_case"
    print("test_dir:",test_dir)
    #����discover�����Ĳ���
    discover= unittest.defaultTestLoader.discover(

            test_dir,
            pattern = 'test*.py',
            top_level_dir = None

            )

        
    return testunit


#3---���Ա���
now = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))

#�����������·����֧�����·����
report = os.path.join(os.getcwd(), "report\\")
print(report)
filename = report+now+'result.html'
fp = open(filename, 'wb')
runner =HTMLTestRunner.HTMLTestRunner(
    stream=fp,
    title='guanlihoutai_test_report',
    description=u'test_case_description')



if __name__ == '__main__':
    #����creatsuite������������Ҫ��ӵ�test*.py�ļ���ɵĲ����׼�
    alltestnames = creatsuite()
    runner.run(alltestnames)
    fp.close()
