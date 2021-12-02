#coding:utf-8

import unittest,requests
from base.runmethod import RunMethod
from data import data_config


class test_Ae(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass

    #老师同意(拒绝)加入操作接口
    def test_send(self):
        url = data_config.get_baseurl() + "/sms/send"
        data = {
                "phone": "13681319134",
                "type": "1",
                }

        headers = data_config.get_headers()
        method = "POST"
        cookies = None
        res = RunMethod().run_main(url, method, data, cookies, headers)
        print(res)
        self.assertEqual(res["status"], 0, msg="测试不通过")
    #教师查看邀请详情接口
    # def test_invitationInfo(self):
    #     url = data_config.get_baseurl()+"japi/orgUserTeacher/invitationInfo?invite_type=1&invite_id=767"
    #     data = None
    #     cookies = {}
    #     headers = data_config.get_headers()
    #     method = "GET"
    #     cookies = None
    #     res = RunMethod().run_main(url, method, data, cookies, headers)
    #     print(res)
    #     self.assertEqual(res["status"],0,msg="测试不通过")


if __name__ == "__main__":
    unittest.main()




