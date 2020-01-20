class Log:

    def __init__(self):
        print("init")


    def setContext(self,con):
        cur = con.cursor()
        cur.callproc("pkg_test_class.set_context",[11,])


    def writeLog(self,con):
        cur = con.cursor()
        cur.callproc("pkg_test_class.set_writelog",['test',])


