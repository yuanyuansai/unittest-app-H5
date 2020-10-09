import pymysql.cursors
import json
class OperationMysql:
    def __init__(self):
        self.conn = pymysql.connect(
            host = 'localhost',
            port = 3306,
            user = 'root',
            password = '111111',
            db = 'learn',
            charset = 'utf8',
            cursorclass = pymysql.cursors.DictCursor
            )
        self.cur = self.conn.cursor()
    def search_one(self,sql):
        self.cur.execute(sql)
        result = self.cur.fetchone()
        result = json.dumps(result)
        return result

if __name__ == '__main__':
    op_mysql = OperationMysql()
    res = op_mysql.search_one("select * from class")
    print(res)