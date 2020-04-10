import os
import sys
import fnmatch
import shutil

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

# Loop through files 

print("Loop through files in " + directory + "\n")

for filename in os.listdir(directory):
    if os.path.isdir(directory + '\\' + filename):
        print(filename + " is a directory "  )
    else:
        if fnmatch.fnmatch(filename, '*-DI-*Material*'):
            try:
                os.rename(directory + '\\' + filename, di_mkt_tgt_dir + '\\' + filename)
                print(filename + " moved to " + di_mkt_tgt_dir)
            except:
                print(filename + " already present at " + di_mkt_tgt_dir)
        elif fnmatch.fnmatch(filename, '*-DI-*Cross*'):
            try:
                os.rename(directory + '\\' + filename, di_cross_tgt_dir + '\\' + filename)
                print(filename + " moved to " + di_cross_tgt_dir)
            except:
                print(filename + " already present at " + di_cross_tgt_dir)
        elif fnmatch.fnmatch(filename, '*-FP-*Material*'):
            try:
                os.rename(directory + '\\' + filename, fp_mkt_tgt_dir + '\\' + filename)
                print(filename + " moved to " + fp_mkt_tgt_dir)
            except:
                print(filename + " already present at " + fp_mkt_tgt_dir)
        elif fnmatch.fnmatch(filename, '*-FP-*Cross*'):
            try:
                os.rename(directory + '\\' + filename, fp_cross_tgt_dir + '\\' + filename)
                print(filename + " moved to " + fp_cross_tgt_dir)
            except:
                print(filename + " already present at " + fp_cross_tgt_dir)            
        elif fnmatch.fnmatch(filename, '*-IT-*Cross*'):
            try:
                os.rename(directory + '\\' + filename, it_cross_tgt_dir + '\\' + filename)
                print(filename + " moved to " + it_cross_tgt_dir)
            except:
                print(filename + " already present at " + it_cross_tgt_dir)
        elif fnmatch.fnmatch(filename, '*-PIA-*Cross*'):
            try:
                os.rename(directory + '\\' + filename, pia_cross_tgt_dir + '\\' + filename)
                print(filename + " moved to " + pia_cross_tgt_dir)
            except:
                print(filename + " already present at " + pia_cross_tgt_dir)
        elif fnmatch.fnmatch(filename, '*-PIC-*Cross*'):
            try:
                os.rename(directory + '\\' + filename, pic_cross_tgt_dir + '\\' + filename)
                print(filename + " moved to " + pic_cross_tgt_dir)
            except:
                print(filename + " already present at " + pic_cross_tgt_dir)
        elif fnmatch.fnmatch(filename, '*-PT-*Cross*'):
            try:
                os.rename(directory + '\\' + filename, pt_cross_tgt_dir + '\\' + filename)
                print(filename + " moved to " + pt_cross_tgt_dir)
            except:
                print(filename + " already present at " + pt_cross_tgt_dir)
            
        else:
            print(filename + " does not satisfy any pattern hence not moved. ")

