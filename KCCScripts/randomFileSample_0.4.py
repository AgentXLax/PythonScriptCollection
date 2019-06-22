##Author: Nathan Wisla
##Last Updated: 6/22/2019

import os
import shutil
from random import choice
from datetime import datetime


##PARAMETERS##
##SOURCE OF TRP FILES (FROM HDD)(use '/' or '\\')##
srcRoot =  'D:\\23610009_CUS_Rogers_Network_Optimization_Program\\CA_Campaign_01\\System1\\Raw_Data'
##DESTINATION OF DUMP (use '/' or '\\')##
dstRoot = 'D:\\Dump'
##################################################
date = datetime.today().strftime('%Y-%m-%d')

##TESTS##
##date = '2019-06-05'
##root = 'C:\\Users\\Nathan\\Desktop\\fileSamplerPG'
##srcRoot = os.path.join(root,'sample_root')
##dstRoot = os.path.join(root,'destination_root')
##################################################




##################################CODE###############################
trpBundle = []
##navigate to the root of the trp files
##first to the root for each client's data
for folder in os.listdir(srcRoot):
    #in case the specific date directory doesn't exist, keep checking other directories
    #it is a FileNotFoundError, but I just made a sweeping catch-all
    try:
        hourRoot = os.path.join(srcRoot,folder,'success',date)
        for hour in os.listdir(hourRoot):
            trpList = []
            trpPath = os.path.join(hourRoot,hour)
            for file in os.listdir(trpPath):
                #Directory to pull the .trp files from
                if (file[-4:] == '.trp'):
                    trpList.append(file)

        #after the trp list is created, make a path to 3 of those
        #files at random to be pulled later
            i = 0        
            while(i < 3):
                randomFile = os.path.join(trpPath,choice(trpList))
                if(randomFile not in trpBundle):
                    trpBundle.append(randomFile)
                    i += 1
                #closes loop if a folder happens to have less than 3 .trp files    
                if(len(trpList) <= 3):
                    i += 1

    except(FileNotFoundError):
        continue

##trpBundle now has the paths to all .trp files in the source folder.
##copy them over to the destination
            
##check if the directory exists
if(not os.path.exists(dstRoot)):
    print('creating destination folder at',dstRoot)
    os.mkdir(dstRoot)
##remove files from the destination if it isn't empty
elif(len(os.listdir(dstRoot)) != 0):
    for file in os.listdir(dstRoot):
        print('removing',file)
        os.remove(os.path.join(dstRoot,file))

for src in trpBundle:
    print(os.path.split(src)[1],'copied to',dstRoot)
    shutil.copy(src,dstRoot)
