import requests

class RunMethod:

    def send_get(self,url,cookies=None,headers=None):

        res = requests.get(url,cookies=cookies,headers=headers,verify=False)
        return res

    def send_post(self,url,data=None,cookies=None,headers=None):

        res = requests.post(url,data=data,cookies=cookies,headers=headers,verify=False)
        return res

    def run_main(self,url,method,data=None,cookies=None,headers=None):

        requests.packages.urllib3.disable_warnings()
        res = None


        if method == 'GET':
            res = self.send_get(url,cookies,headers)
        else:
            res = self.send_post(url,data=data,cookies=cookies,headers=headers)

        #响应的捕捉异常
        res1=None
        try:
            res1=res.json()
        except Exception as e:
            print("这是异常")
            print(e)
            print("这是异常")

        return res1
if __name__ == '__main__':
    url = "https://api-dev.1911edu.com/api/v1/wallet/get_data/2"
    data = None
    cookies = {'authorization': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiMjAwMDAwMTQ5IiwidXNlcl90eXBlIjoxLCJjaGFubmVsIjoiYXBwIiwiaWF0IjoxNjEzNDcwODY5LCJleHAiOjE2MTYwNjI4Njl9.ubEuNNLDQX2QcxvZpvr67O0R0WKB2eka1dLnAzlV_9sv853'}
    headers = {'authorization': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiMjAwMDAwMTQ5IiwidXNlcl90eXBlIjoxLCJjaGFubmVsIjoiYXBwIiwiaWF0IjoxNjEzNDcwODY5LCJleHAiOjE2MTYwNjI4Njl9.ubEuNNLDQX2QcxvZpvr67O0R0WKB2eka1dLnAzlV_9sv853'}
    method="GET"
    cookies=None
    r=RunMethod().run_main(url, method, data,cookies,headers)
    # r=requests.get(url,headers=headers,verify=False)
    print(r)

