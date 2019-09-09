import sqlparse
import os
import sys

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




