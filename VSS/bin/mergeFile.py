import sys
import os
import logging
#----------------------------------------------
logging.basicConfig(format='%(levelname)s:%(message)s',level=logging.INFO)
#----------------------------------------------
script_path = os.path.realpath(__file__).split("\\")
inbound_path = "\\".join(script_path[:-2]) + r"\inbound"
outbound_path = "\\".join(script_path[:-2]) + r"\outbound"
logging.info("Script Path is -> " + os.path.realpath(__file__))
logging.info("Inbound Path is -> " + inbound_path)
logging.info("Outbound Path is -> " + outbound_path)
#----------------------------------------------
final_data = []
for all_file in os.listdir(inbound_path):
    logging.info("Processing => " + inbound_path + "\\" + all_file)
    with open(inbound_path + "\\" + all_file, 'r') as rf:
        in_data = [line.rstrip() for line in rf]
    for rec in in_data:    
        final_data.append(rec)
    in_data = []
# logging.info(final_data)
with open(outbound_path + "\\" + "merged_file.dat", "w") as wf:
    for all_rec in final_data:
        wf.writelines(all_rec + "\n")

