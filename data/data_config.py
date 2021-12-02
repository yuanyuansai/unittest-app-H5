'''
开发环境 https://api-dev.1911edu.com/japi 生产环境 https://api.1911edu.com/japi
'''
class global_var:
    headers = {
        'authorization': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX3R5cGUiOiIxIiwidXNlcl9pZCI6IjIwMDAwMjE4NiIsImNoYW5uZWwiOiJhcHAiLCJleHAiOjE2MjI0NzQ0MTQsImlhdCI6MTYyMTU4NTM4MX0.QOPZiZIwUFm44pkNMxZVZDiFiY583jbaQF8kM4sYnksa8a3'}
    baseurl="https://api-dev.1911edu.com/"


def get_headers():
    return global_var.headers
def get_baseurl():
    return global_var.baseurl