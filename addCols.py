import pandas as pd
import os

directory = 'D:\\learning\\code\\utils\\addColumnExcel'

for filename in os.listdir(directory):
    if filename.endswith(".csv"):
        try:
            with open(directory + '\\' + filename) as input_file:
                # header = input_file.readline()
                data = pd.read_csv(input_file, sep=",")
            data.insert(4, "New Data", 10)

            with open(directory + '\\' + filename, "w") as output_file:
                # output_file.write(header)
                data.to_csv(output_file, index=False,line_terminator="\n")
        except:
            pass
