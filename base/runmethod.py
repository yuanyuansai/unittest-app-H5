import requests
import json
class RunMethod:

    def send_get(self,url,data):
        res = requests.get(url=url,data=data).json()
        return res

    def send_post(self,url,data):
        res = requests.post(url = url,data = data).json()
        return res

    def run_main(self,url,method,data=None):
        res = None
        print(url)

        if method == 'GET':
            res = self.send_get(url,data)
        else:
            res = self.send_post(url,data)
        return res


