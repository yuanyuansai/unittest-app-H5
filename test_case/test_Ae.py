#coding:utf-8
import requests
import os,HTMLTestRunner
import unittest, time, re
from base.runmethod import RunMethod


#/adminapi/api/admin_v1/t_user_franchise_request/search_first?phone_no=&create_begin_time=&create_end_time=&payer_name=&name=&update_begin_time=&update_end_time=&status=&phone=&institution_name=&category=&pay_begin_time=&pay_end_time=&pay_status=&page=1&limit=10&order_by=
class test_Ae(unittest.TestCase):
    
    def setUp(self):
        pass

    def test_reg(self):
        url = "https://api-dev.1911edu.com/api/v1/wallet/get_data/2"
        data = None
        cookies = {
            'authorization': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiMjAwMDAwMTQ5IiwidXNlcl90eXBlIjoxLCJjaGFubmVsIjoiYXBwIiwiaWF0IjoxNjEzNDcwODY5LCJleHAiOjE2MTYwNjI4Njl9.ubEuNNLDQX2QcxvZpvr67O0R0WKB2eka1dLnAzlV_9sv853'}
        headers = {
            'authorization': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiMjAwMDAwMTQ5IiwidXNlcl90eXBlIjoxLCJjaGFubmVsIjoiYXBwIiwiaWF0IjoxNjEzNDcwODY5LCJleHAiOjE2MTYwNjI4Njl9.ubEuNNLDQX2QcxvZpvr67O0R0WKB2eka1dLnAzlV_9sv853'}
        method = "GET"
        cookies = None
        r = RunMethod().run_main(url, method, data, cookies, headers)
        if isinstance(r, dict) and r['status'] == 0:
            print (u'测试通过')
        else:
            print (u'测试失败')



            

    def tearDown(self):
        pass
        
if __name__ == "__main__":
    unittest.main()
    print(1)



