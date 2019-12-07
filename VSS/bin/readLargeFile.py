import pandas as pd

i = 1 

for chunks in pd.read_csv('largefile.csv',chunksize=1000000):

    chunks.to_csv('D:\\learning\\code\\utils\\VSS\\outbound\\partfile'+str(i)+'.csv')
    i += 1