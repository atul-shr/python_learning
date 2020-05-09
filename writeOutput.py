import json
import os
import sys

#==============================

with open('diff.json','r') as rf:
    output = rf.read()

diff_rec = json.loads(output)
wf = open('output.txt','w')

wf.writelines('\n' + '#===========================================================#'+ '\n')    
wf.writelines('#======Column Differences===================================#'+ '\n')    
wf.writelines('#===========================================================#'+ '\n')

for changed_rec in diff_rec['changed']:
    varKey = changed_rec['key']
    varVal = changed_rec['fields']
    for keyRec,keyVal in varVal.items():
        #print('Key Column - ' + str(varKey)[1:-1] +' Column Name - ' + keyRec + ' - Diff - ' + str(keyVal))
        wf.writelines(('Key Column - ' + str(varKey)[1:-1] +' Column Name - ' + keyRec + ' - Diff - ' + str(keyVal)) + '\n')

wf.writelines('\n' + '#===========================================================#'+ '\n')    
wf.writelines('#========Additional Records in Left file====================#'+ '\n')    
wf.writelines('#===========================================================#'+ '\n')    
add_list = []
for add_rec in diff_rec['added']:
#    print(add_rec)
    for add_col,add_val in add_rec.items():
        add_list.append(add_val)
    #print(add_list)
    wf.writelines(str(add_list)[1:-1] + '\n')
wf.writelines('\n' + '#===========================================================#'+ '\n')    
wf.writelines('#=========Additional Records in Right file==================#'+ '\n')    
wf.writelines('#===========================================================#'+ '\n')

del_list = []    
for del_rec in diff_rec['removed']:
#    print(del_rec)
    for del_col,del_val in del_rec.items():
       del_list.append(del_val)
    #print(del_list)
    wf.writelines(str(del_list)[1:-1] + '\n')

wf.writelines('\n' + '#===========================================================#'+ '\n')
#==============================#
wf.close()
