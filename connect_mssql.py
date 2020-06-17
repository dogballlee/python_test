import pymssql as ms

class MSSQL:
    def __init__(self, host, user, pwd, db):  # 类的构造函数，初始化数据库连接ip或者域名，以及用户名，密码，要连接的数据库名称
        self.host = host
        self.user = user
        self.pwd = pwd
        self.db = db

    def __getconnect(self):  # 得到数据库连接信息函数， 返回: conn.cursor()
        if not self.db:
            raise(NameError, "没有设置数据库信息")
        self.conn = ms.connect(host=self.host, user=self.user, password=self.pwd, database=self.db, charset='utf8')
        cur = self.conn.cursor()  # 将数据库连接信息，赋值给cur。
        if not cur:
            raise(NameError, "连接数据库失败")
        else:
            return cur

    def execquery(self,sql):  # 执行Sql语句函数，返回结果
        cur = self.__getconnect()  # 获得数据库连接信息
        cur.execute(sql)  # 执行Sql语句
        reslist = cur.fetchall()  # 获得所有的查询结果
        self.conn.close()  # 查询完毕后必须关闭连接
        return reslist  # 返回查询结果

    def execnonquery(self,sql):
        cur = self.__getconnect()
        cur.execute(sql)
        self.conn.commit()
        self.conn.close()

mss = MSSQL(host='xxx.xx.xx.xx\xxxxxxxxx', user='sa', pwd='Password01!', db='REPORT_SOURCE')
sql = '''select convert(varchar(10),pay_time,120) pt,count(order_no) 
            from Order_Info 
            where order_status in(2,3,7,8) and real_amount > 100 and course_name = '某某某某' 
            group by convert(varchar(10),pay_time,120)'''
reslist = mss.execquery(sql)