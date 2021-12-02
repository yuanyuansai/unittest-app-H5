import requests,json
# for i in range(1):
#
#     url = "http://ldym.xpqmmf.cn/ceshi/ainfoDetailNew_b187_x30790?sid=oJN3_5meUbHYeFrNHSTrjLmgdOxk"
#     data = {
#     }
#     cookies = None
#     headers = {
#         'authorization': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX3R5cGUiOiIxIiwidXNlcl9pZCI6IjYxNiIsImNoYW5uZWwiOiJhcHAiLCJleHAiOjE2MjM4NDA5OTIsImlhdCI6MTYyMzIzNjE5Mn0.YL12oia-yaI-1B9VenWEtnXaYkjdmvGGYCuJm_N-Q8Elst4'}
#     method = "GET"
#     res = requests.get(url, cookies=cookies, headers=headers, verify=False)
#     print(res.text)

for i in range(1):
    url = "http://ldym.xpqmmf.cn/ceshi/afree"
    data = {
        'buynum': '1',
        'openid': 'oJN3_5njOlVLA8s2DQyanePzSfKI',
        'userid': '273076',  #273076
        'xs_id': '30790',
        'inputPiaoshu': '1',
        'lw_id': '1',
        'hd_id': '187',
    }
    cookies = None
    headers = {
        'authorization': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX3R5cGUiOiIxIiwidXNlcl9pZCI6IjYxNiIsImNoYW5uZWwiOiJhcHAiLCJleHAiOjE2MjM4NDA5OTIsImlhdCI6MTYyMzIzNjE5Mn0.YL12oia-yaI-1B9VenWEtnXaYkjdmvGGYCuJm_N-Q8Elst4'}
    method = "POST"
    res = requests.post(url, data=data, cookies=cookies, headers=headers, verify=False)

    print(json.loads(res.content))





