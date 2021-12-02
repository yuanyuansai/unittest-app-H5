#coding:utf-8

import unittest
from base.runmethod import RunMethod
from data import data_config


class test_Ae(unittest.TestCase):
    #刘栋7.2的接口
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

    #公开课列表
    def test_orgOperation(self):
        url = data_config.get_baseurl() + "/publicCourse/myBuyList"
        data = {}
        cookies = {}
        headers = data_config.get_headers()
        method = "GET"
        cookies = None
        res = RunMethod().run_main(url, method, data, cookies, headers)
        print(res)
        self.assertEqual(res["status"], 0, msg="测试不通过")



if __name__ == "__main__":
    unittest.main()




