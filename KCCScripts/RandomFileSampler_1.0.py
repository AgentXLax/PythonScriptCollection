##Author: Nathan Wisla
##Last Updated: 8/18/2019

import os
import shutil
from random import choice
import datetime

class FileSampler:

    def __init__(self,srcRoot,dstRoot,date):
        self.srcRoot = srcRoot
        self.dstRoot = dstRoot
        self.date = date
        self.startDateTime = self.findWorkDay(date)[0]
        self.endDateTime = self.findWorkDay(date)[1] #find the startTime and endTime
        self.trpCollection = self.trpWalk()
        self.dstExists = os.path.exists(dstRoot)

    ##walk through the folder structure to find the start and end times           
    def findWorkDay(self,endDate):
        '''return startDateTime, endDateTime (datetime objects)
        '''
        srcRoot = self.srcRoot
        startDate = (endDate - datetime.timedelta(1))
        hours = os.listdir(os.path.join(srcRoot,'client11_Rogers','success',startDate.strftime('%Y-%m-%d')))
        startTime = -1
        endTime = -1
        
        for i in range(len(hours)):
            if len(hours) == 1:
                startTime = hours[0]
            if float(hours[i])-float(hours[i-1]) > 1:
                startTime = hours[i]
                break
        hours = os.listdir(os.path.join(srcRoot,'client11_Rogers','success',endDate.strftime('%Y-%m-%d')))
        if startTime == -1:
            startDate = endDate
            startTime = hours[0]
        endTime = hours[-1]
        startDateTime = datetime.datetime(startDate.year,startDate.month,startDate.day,int(startTime[:-3]))
        endDateTime = datetime.datetime(endDate.year,endDate.month,endDate.day,int(endTime[:-3]))
        return startDateTime,endDateTime
     
    def trpWalk(self):
        startTime = self.startDateTime.strftime('%H.00')
        startDate = self.startDateTime.strftime('%Y-%m-%d')
        endDate = self.endDateTime.strftime('%Y-%m-%d')
        srcRoot = self.srcRoot
        dstRoot = self.dstRoot
        needsStart = startDate != endDate

        trpCollection = []
        
        for client in os.listdir(srcRoot):
            try:
                 hourRoot = os.path.join(srcRoot,client,'success',startDate)
                 if needsStart:
                     startFound = False
                     for hour in os.listdir(hourRoot):
                         if hour == startTime:
                             startFound = True
                         
                         if startFound:
                             trpAtSrc = []
                             trpPath = os.path.join(hourRoot,hour)
                             self.trpCollect(trpPath,trpAtSrc)
                             self.trpTripleRandomize(trpPath,trpAtSrc,trpCollection)
                     hourRoot = os.path.join(srcRoot,client,'success',endDate)
                 for hour in os.listdir(hourRoot):    
                     trpAtSrc = []
                     trpPath = os.path.join(hourRoot,hour)
                     self.trpCollect(trpPath,trpAtSrc)
                     self.trpTripleRandomize(trpPath,trpAtSrc,trpCollection)    

            except(FileNotFoundError):
                continue
        return trpCollection

    def trpCollect(self,src,srcFiles):
        for file in os.listdir(src):
            if file[-4:] == '.trp':
                srcFiles.append(file)
        
    def trpTripleRandomize(self,src,srcFiles,collection):
        i = 0        
        while(i < 3):
            try:
                randomFile = os.path.join(src,choice(srcFiles))
                if randomFile not in collection:
                    collection.append(randomFile)
                    i += 1
                if len(srcFiles) < 3:
                    i += 1

            except(IndexError):
                break #in case of an empty list, choice() will fail

    def createDst(self):
        print('creating destination folder at',dstRoot)
        os.mkdir(dstRoot)
        print('Dump folder successfully created!')

    def clearDst(self):
        for file in os.listdir(self.dstRoot):
            dst = os.path.join(self.dstRoot,file)
            if os.path.isdir(dst):
                print('removing directory',file)
                shutil.rmtree(dst)
            else:
                print('removing file',file)
                os.remove(dst)
        print('Dump folder successfully emptied!')
    
    def dump(self):
        if not self.dstExists:
            self.createDst()
        elif len(os.listdir(self.dstRoot)) != 0:
            self.clearDst()
        for src in self.trpCollection:
            print(os.path.split(src)[1],'copied to',self.dstRoot)
            shutil.copy(src,self.dstRoot)
        print('Files successfully copied!')

    def __repr__(self):
        aStr = '.trp file dump from ' +\
               self.startDateTime.strftime('%Y-%m-%d %H.00') +\
               ' until ' +\
               self.endDateTime.strftime('%Y-%m-%d %H.00')
        return aStr
