#coding:utf-8

import unittest
from base.runmethod import RunMethod
from data import data_config


class test_Ae(unittest.TestCase):
    #乃江的接口
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

    #机构对老师审核接口
    def test_orgOperation(self):
        url = data_config.get_baseurl() + "japi/teacherUser/orgOperation"
        data = {"oper_type": 1,
                "teacher_user_id": "",
                "audit_remarks": "",
                }
        cookies = {}
        headers = data_config.get_headers()
        method = "POST"
        cookies = None
        res = RunMethod().run_main(url, method, data, cookies, headers)
        print(res)
        self.assertEqual(res["status"], 0, msg="测试不通过")
    #机构解绑现有教师接口
    def test_removeBind(self):
        url = data_config.get_baseurl() + "japi/teacherUser/removeBind"
        data = {
                "teacher_user_id": "12321",
                }
        cookies = {}
        headers = data_config.get_headers()
        method = "POST"
        cookies = None
        res = RunMethod().run_main(url, method, data, cookies, headers)
        print(res)
        self.assertEqual(res["status"], 0, msg="测试不通过")
    #老师同意(拒绝)加入操作接口
    def test_teacherOperation01(self):
        url = data_config.get_baseurl() + "japi/teacherUser/teacherOperation"
        data = {
                "oper_type": 1,  #同意
                "invite_id": 1234,
                "audit_remarks": "",
                "invite_type": "1",
                }
        cookies = {}
        headers = data_config.get_headers()
        method = "POST"
        cookies = None
        res = RunMethod().run_main(url, method, data, cookies, headers)
        print(res)
        self.assertEqual(res["status"], 0, msg="测试不通过")

    #老师同意(拒绝)加入操作接口
    def test_teacherOperation02(self):
        url = data_config.get_baseurl() + "japi/teacherUser/teacherOperation"
        data = {
                "oper_type": 2,  #拒绝
                "invite_id": 1234,
                "audit_remarks": "",
                "invite_type": "1",
                }
        cookies = {}
        headers = data_config.get_headers()
        method = "POST"
        cookies = None
        res = RunMethod().run_main(url, method, data, cookies, headers)
        print(res)
        self.assertEqual(res["status"], 0, msg="测试不通过")
    #教师查看邀请详情接口
    def test_invitationInfo(self):
        url = data_config.get_baseurl()+"japi/orgUserTeacher/invitationInfo?invite_type=1&invite_id=767"
        data = None
        cookies = {}
        headers = data_config.get_headers()
        method = "GET"
        cookies = None
        res = RunMethod().run_main(url, method, data, cookies, headers)
        print(res)
        self.assertEqual(res["status"],0,msg="测试不通过")

    #机构查询本单位下教师(审核通过)接口
    def test_searchMyTeacher01(self):
        url = data_config.get_baseurl()+"japi/teacherUser/searchMyTeacher"
        data = {"searchkey":"这是建议内容",
                "page":1,
                "limit":10,
                }
        cookies = {}
        headers = data_config.get_headers()
        method = "POST"
        cookies = None
        r = RunMethod().run_main(url, method, data, cookies, headers)
        print(r)
        self.assertEqual(r["status"],0,msg="测试不通过")

    # 机构查询本单位下教师(审核通过)接口
    def test_searchMyTeacher02(self):
        url = data_config.get_baseurl()+"japi/teacherUser/searchMyTeacher?searchkey='123'&page=1&limit=10"
        data = None
        cookies = {}
        headers = data_config.get_headers()
        method = "GET"
        cookies = None
        res = RunMethod().run_main(url, method, data, cookies, headers)
        print(res)
        self.assertEqual(res["status"],0,msg="测试不通过")
    #地区查询接口
    def test_fetchDataByFatherId(self):
        url = data_config.get_baseurl()+"japi/district/fetchDataByFatherId?fatherId=320000"
        data = None
        cookies = {}
        headers = data_config.get_headers()
        method = "GET"
        cookies = None
        res = RunMethod().run_main(url, method, data, cookies, headers)
        print(res)
        self.assertEqual(res["status"],0,msg="测试不通过")
    #我的基本统计信息查询接口
    def test_getMyStatisticsInfo(self):
        url = data_config.get_baseurl()+"japi/myInfo/getMyStatisticsInfo"
        data = None
        cookies = {}
        headers = data_config.get_headers()
        method = "POST"
        cookies = None
        r = RunMethod().run_main(url, method, data, cookies, headers)
        print(r)
        self.assertEqual(r["status"],0,msg="测试不通过")
    #用户安全设置信息查询
    def test_getAccountSafeInfo(self):
        url = data_config.get_baseurl()+"japi/user/getAccountSafeInfo"
        data = None
        cookies = {}
        headers = data_config.get_headers()
        method = "POST"
        cookies = None
        res = RunMethod().run_main(url, method, data, cookies, headers)
        print(res)
        self.assertEqual(res["status"],0,msg="测试不通过")
    #检测单位名称是否被使用接口
    def test_checkNickName(self):
        url = data_config.get_baseurl()+"japi/user/checkNickName"
        data = {"nick_name":"asdhasudha"}
        cookies = {}
        headers = data_config.get_headers()
        method = "POST"
        cookies = None
        res = RunMethod().run_main(url, method, data, cookies, headers)
        print(res)
        self.assertEqual(res["status"],0,msg="测试不通过")
    #机构提交资质认证
    def test_addCertInfo(self):
        url = data_config.get_baseurl()+"japi/orgUser/addCertInfo"
        data = {"license_images":"https://ceshi-image.1911edu.com/4b3aba5b-12be-322d-ec2d-3913a42cc1da.jpg",
                "name":"jigouname"}
        cookies = {}
        headers = data_config.get_headers()
        method = "POST"
        cookies = None
        res = RunMethod().run_main(url, method, data, cookies, headers)
        print(res)
        self.assertEqual(res["status"],0,msg="测试不通过")

    #建议反馈接口
    def test_addCertInfo(self):
        url = data_config.get_baseurl()+"japi/suggestFeedback/addSuggestInfo"
        data = {"suggest_content":"这是建议内容",
                "contact_phone":"13681319134",
                "suggest_images":"https://ceshi-image.1911edu.com/4b3aba5b-12be-322d-ec2d-3913a42cc1da.jpg",
                "platform":1,
                "device_model":"13681319134",
                "net_type":2,
                "client_version":"7.0.0",
                "system_version":"123",
                }
        cookies = {}
        headers = data_config.get_headers()
        method = "POST"
        cookies = None
        res = RunMethod().run_main(url, method, data, cookies, headers)
        print(res)
        self.assertEqual(res["status"],0,msg="测试不通过")
        #获取机构资质认证详情
    def test_findcertInfo(self):
        url = data_config.get_baseurl()+"japi/orgUser/findcertInfo"
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




