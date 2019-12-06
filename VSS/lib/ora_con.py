import cx_Oracle as cx

class dbCon:

    def __init__(self,usr,pwd,sid):
        self.usr = usr
        self.pwd = pwd
        self.sid = sid
        self.tns = usr + '/' + pwd + '@' + sid
        print('Tns is ' , self.tns)

    def createConnection(self):
        self.con = cx.connect(self.tns)
        return self.con

    def createCursor(self,con):
        self.cur = con.cursor()
        return self.cur
