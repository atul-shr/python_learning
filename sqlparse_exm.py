import sqlparse
import os
import sys

def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""

def find_between_r( s, first, last ):
    try:
        start = s.rindex( first ) + len( first )
        end = s.rindex( last, start )
        return s[start:end]
    except ValueError:
        return ""

for config_file in os.listdir("C:\\Users\\atul.shr\\PycharmProjects\\PyShop\\testing\\config"):
    with open("C:\\Users\\atul.shr\\PycharmProjects\\PyShop\\testing\\config\\" + config_file,"r") as cnf_r :
        for lines in cnf_r:
            if lines.startswith("sqlfilename"):
                sql_file = lines.split("/")[1]
                cwd = os.getcwd()
                #os.chdir(cwd + "\\sql\\"+sql_file[:-1])
                with open(cwd + "\\sql\\"+sql_file.rstrip("\n"),"r") as sqlf:
                    sqls = sqlf.read().rstrip("\n")
                    #print(sqls)
                    print(sqlparse.format(sqls, keyword_case="upper", reindent=True))
                    print(find_between(sqls,"select","from"))




