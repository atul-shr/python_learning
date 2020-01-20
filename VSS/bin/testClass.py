import cx_Oracle
import Log as lg


conn = cx_Oracle.connect("pharma/pharma@LAPTOP-21RC5VEQ:1521/XE")

log = lg.Log()

log.setContext(conn)

log.writeLog(conn)


