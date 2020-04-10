import os
import sys
import fnmatch
import shutil
from datetime import datetime
from datetime import timedelta
from dateutil.relativedelta import relativedelta
import logging

try:
    logging.basicConfig( filename=os.getcwd()+'\\'+__file__[:-3] +'.log', format='%(asctime)s:%(levelname)s:%(message)s', level=logging.DEBUG)
    logger = logging.getLogger(__name__)
except ValueError:
    pass
    

# Directory Paths 

directory = "C:\\Users\\atul.shr\\Documents\\Email Attachments"
di_mkt_tgt_dir = "C:\\Users\\atul.shr\\Documents\\Email Attachments\\DI"
di_cross_tgt_dir = "C:\\Users\\atul.shr\\Documents\\Email Attachments\\DI"
it_cross_tgt_dir = "C:\\Users\\atul.shr\\Documents\\Email Attachments\\IT"
pia_cross_tgt_dir = "C:\\Users\\atul.shr\\Documents\\Email Attachments\\PIA"
fp_mkt_tgt_dir = "C:\\Users\\atul.shr\\Documents\\Email Attachments\\FP"
fp_cross_tgt_dir = "C:\\Users\\atul.shr\\Documents\\Email Attachments\\FP"
pic_cross_tgt_dir = "C:\\Users\\atul.shr\\Documents\\Email Attachments\\PIC"
pt_cross_tgt_dir = "C:\\Users\\atul.shr\\Documents\\Email Attachments\\PT"

def get_month_day_range(date):
    last_day = date + relativedelta(day=1, months=+1, days=-1)
    first_day = date + relativedelta(day=1)
    return first_day, last_day

today = datetime.today()
first = today.replace(day=1)
lastMonth = first - timedelta(days=1)

firstLastMonth, LastLastMonth = get_month_day_range(lastMonth)

# Loop through files 

logger.info("Loop through files in " + directory + "\n")

for filename in os.listdir(directory):
    if os.path.isdir(directory + '\\' + filename):
        logger.info(filename + " is a directory " )
    else:
        if datetime.strptime(filename[:10],'%Y-%m-%d')>=  firstLastMonth.replace(hour=0, minute=0, second=0, microsecond=0) and datetime.strptime(filename[:10],'%Y-%m-%d') <= LastLastMonth.replace(hour=0, minute=0, second=0, microsecond=0):
            if fnmatch.fnmatch(filename, '*-DI-*Material*'):
                try:
                    os.rename(directory + '\\' + filename, di_mkt_tgt_dir + '\\' + filename)
                    logger.info(filename + " moved to " + di_mkt_tgt_dir)
                except:
                    logger.info(filename + " already present at " + di_mkt_tgt_dir)
            elif fnmatch.fnmatch(filename, '*-DI-*Cross*'):
                try:
                    os.rename(directory + '\\' + filename, di_cross_tgt_dir + '\\' + filename)
                    logger.info(filename + " moved to " + di_cross_tgt_dir)
                except:
                    logger.info(filename + " already present at " + di_cross_tgt_dir)
            elif fnmatch.fnmatch(filename, '*-FP-*Material*'):
                try:
                    os.rename(directory + '\\' + filename, fp_mkt_tgt_dir + '\\' + filename)
                    logger.info(filename + " moved to " + fp_mkt_tgt_dir)
                except:
                    logger.info(filename + " already present at " + fp_mkt_tgt_dir)
            elif fnmatch.fnmatch(filename, '*-FP-*Cross*'):
                try:
                    os.rename(directory + '\\' + filename, fp_cross_tgt_dir + '\\' + filename)
                    logger.info(filename + " moved to " + fp_cross_tgt_dir)
                except:
                    logger.info(filename + " already present at " + fp_cross_tgt_dir)            
            elif fnmatch.fnmatch(filename, '*-IT-*Cross*'):
                try:
                    os.rename(directory + '\\' + filename, it_cross_tgt_dir + '\\' + filename)
                    logger.info(filename + " moved to " + it_cross_tgt_dir)
                except:
                    logger.info(filename + " already present at " + it_cross_tgt_dir)
            elif fnmatch.fnmatch(filename, '*-PIA-*Cross*'):
                try:
                    os.rename(directory + '\\' + filename, pia_cross_tgt_dir + '\\' + filename)
                    logger.info(filename + " moved to " + pia_cross_tgt_dir)
                except:
                    logger.info(filename + " already present at " + pia_cross_tgt_dir)
            elif fnmatch.fnmatch(filename, '*-PIC-*Cross*'):
                try:
                    os.rename(directory + '\\' + filename, pic_cross_tgt_dir + '\\' + filename)
                    logger.info(filename + " moved to " + pic_cross_tgt_dir)
                except:
                    logger.info(filename + " already present at " + pic_cross_tgt_dir)
            elif fnmatch.fnmatch(filename, '*-PT-*Cross*'):
                try:
                    os.rename(directory + '\\' + filename, pt_cross_tgt_dir + '\\' + filename)
                    logger.info(filename + " moved to " + pt_cross_tgt_dir)
                except:
                    logger.info(filename + " already present at " + pt_cross_tgt_dir)
                
            else:
                logger.info(filename + " does not satisfy any pattern hence not moved. " + str(datetime.strptime(filename[:10],'%Y-%m-%d')))
        else:
            logger.info(filename + " is older than last month. ")
