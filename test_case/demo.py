#coding:utf-8

import unittest
from base.runmethod import RunMethod
from data import data_config


class test_Ae(unittest.TestCase):

    # @classmethod
    # def setUpClass(cls):
    #     print("类之前的方法")
    #
    # @classmethod
    # def tearDownClass(cls):
    #     print("类之后的方法")
    def setUp(self):
        pass
    def tearDown(self):
        pass

    #用户信息
    def test_teacherOperation02(self):
        url = data_config.get_baseurl() + "/japi/myInfo/getPreInfo"
        data = {}
        cookies = {}
        headers = data_config.get_headers()
        method = "POST"
        cookies = None
        res = RunMethod().run_main(url, method, data, cookies, headers)
        print(res)
        self.assertEqual(res["status"], 0, msg="测试不通过")

    def test_teacherOperation02(self):
        url = data_config.get_baseurl() + "/japi/publicClass/getPublicClasses"
        data = {

        }
        cookies = {}
        headers = data_config.get_headers()
        method = "POST"
        cookies = None
        res = RunMethod().run_main(url, method, data, cookies, headers)
        print(res)
        self.assertEqual(res["status"], 0, msg="测试不通过")
    #学习中心
    def test_teacherOperation02(self):
        url = data_config.get_baseurl() + "/AdultApi/v4_4/MyInfo/myDayStudyCenter"
        data = {}
        cookies = {}
        headers = data_config.get_headers()
        method = "GET"
        cookies = None
        res = RunMethod().run_main(url, method, data, cookies, headers)
        print(res)
        self.assertEqual(res["status"], 0, msg="测试不通过")
    #用户图片信息
    def test_invitationInfo(self):
        url = data_config.get_baseurl()+"/AdultApi/v4_4/UserCenter/generateImageInfo"
        data = None
        cookies = {}
        headers = data_config.get_headers()
        method = "GET"
        cookies = None
        res = RunMethod().run_main(url, method, data, cookies, headers)
        print(res)
        self.assertEqual(res["status"],0,msg="测试不通过")
    #
    def test_invitationInfo(self):
        url = data_config.get_baseurl()+"/AdultApi/v4_4/UserCenter/generateImageInfo"
        data = None
        cookies = {}
        headers = data_config.get_headers()
        method = "GET"
        cookies = None
        res = RunMethod().run_main(url, method, data, cookies, headers)
        print(res)
        self.assertEqual(res["status"],0,msg="测试不通过")


if __name__ == "__main__":
    unittest.main()




