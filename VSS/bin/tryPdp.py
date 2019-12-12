import pandas as pd
import pdpipe as pdp
import cx_Oracle as cx

con = cx.connect('hr/HR@LAPTOP-21RC5VEQ:1521/XE')

df = pd.read_sql('select * from user_tables',con)

def size(n):
       if n == 'NaN':
              return 'Very Small'
       elif n <= 0:
              return 'Small'       
       elif n <= 6:
              return 'Medium'
       elif n > 6 :
              return 'Big'                            

df['BLOCK_SIZE'] = df['BLOCKS'].apply(size)

drop_cols = pdp.ColDrop(['PCT_FREE', 'PCT_USED', 'INI_TRANS', 'MAX_TRANS', 'SEGMENT_CREATED',
       'RESULT_CACHE','INITIAL_EXTENT',
       'NEXT_EXTENT', 'MIN_EXTENTS', 'MAX_EXTENTS', 'PCT_INCREASE',
       'FREELISTS', 'FREELIST_GROUPS', 'LOGGING', 'BACKED_UP', 'NUM_ROWS',
        'EMPTY_BLOCKS', 'AVG_SPACE', 'CHAIN_CNT', 'AVG_ROW_LEN',
       'AVG_SPACE_FREELIST_BLOCKS', 'NUM_FREELIST_BLOCKS', 'DEGREE',
       'INSTANCES', 'CACHE', 'TABLE_LOCK', 'SAMPLE_SIZE', 'LAST_ANALYZED',
       'PARTITIONED', 'IOT_TYPE', 'TEMPORARY', 'SECONDARY', 'NESTED',
       'BUFFER_POOL', 'FLASH_CACHE', 'CELL_FLASH_CACHE', 'ROW_MOVEMENT',
       'GLOBAL_STATS', 'USER_STATS', 'DURATION', 'SKIP_CORRUPT', 'MONITORING',
       'CLUSTER_OWNER', 'DEPENDENCIES', 'COMPRESSION', 'COMPRESS_FOR',
       'DROPPED', 'READ_ONLY'])

drop_cols += pdp.OneHotEncode('BLOCK_SIZE')

df1 = drop_cols(df)

print(df1.columns)    




