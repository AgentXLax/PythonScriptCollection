##Author: Nathan Wisla
##Last Updated: 6/09/2019

import os
import shutil
from random import choice
from datetime import datetime

##PARAMETERS##
##TODAY'S DATE YYYY-MM-DD##
date = datetime.today().strftime('%Y-%m-%d')
##SOURCE OF TRP FILES (FROM HDD)(use fwd slashes '/')##
srcRoot =  'D:/23610009_CUS_Rogers_Network_Optimization_Program/CA_Campaign_01/System1/Raw_Data'
##DESTINATION OF DUMP (use fwd slashes '/')##
dstRoot = 'C:/Users/Nathan/Desktop/DumpPy'
##################################################

##TESTS##
##date = '2019-06-05'
##root = 'C:/Users/Nathan/Desktop/fileSamplerPG'
##srcRoot = os.path.join(root,'sample_root')
##dstRoot = os.path.join(root,'destination_root')
##################################################
##################################CODE###############################
trpBundle = []
##navigate to the root of the trp files
##first to the root for each client's data
for folder in os.listdir(srcRoot):
    ##goes to the date directory
    hourRoot = os.path.join(srcRoot,folder,'success',date)

    for hour in os.listdir(hourRoot):
        trpList = []
        trpPath = os.path.join(hourRoot,hour)
        
        for file in os.listdir(trpPath):
            if (file[-4:] == '.trp'):
                trpList.append(file)

    #after the trp list is created, make a path to of those
    #files at random
        i = 0        
        while(i < 3):
            randomFile = os.path.join(trpPath,choice(trpList))
            
            if(randomFile not in trpBundle):
                trpBundle.append(randomFile)
                i += 1
            if(len(trpList)<3):
                break
##trpBundle now has the paths to all trp files in the source folder.
##copy them over to the destination
            
##print(trpBundle)
for src in trpBundle:
    print(src)
    shutil.copy(src,dstRoot)
