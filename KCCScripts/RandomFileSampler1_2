##Author: Nathan Wisla
##Last Updated: 8/27/2019

import os
import shutil
from random import choice
import datetime

class FileSampler:

    def __init__(self,srcRoot,dstRoot,date=datetime.date.today(),\
                 startEndOverride=False,startDTOR=None,endDTOR=None, backup=True):
        '''
           srcRoot: root of the source where you want to take files from
           dstRoot: root of the desired dump location
           date: datetime.datetime object, defaults to the current date
           override: allows you to override which hour range you want to select, defaults to False
           startDTOR: datetime.datetime object to override the search algorithm
           endDTOR: datetime.datetime object to override the search algorithm
           backup: switches search algorithm to simpler folder search
        '''
        self.srcRoot = srcRoot
        self.dstRoot = dstRoot
        self.date = date
        if startEndOverride:
            self.startDateTime = startDTOR
            self.endDateTime = endDTOR
        else:
            self.startDateTime = self.findWorkDay(date)[0]
            self.endDateTime = self.findWorkDay(date)[1]
        if backup:
            print('backup search enabled')
            self.trpCollection = self.trpWalk(True)
        else:
            self.trpCollection = self.trpWalk()
        self.dstExists = os.path.exists(dstRoot)

         
    def findWorkDay(self,endDate):
        '''return startDateTime, endDateTime (datetime objects)
        '''
        srcRoot = self.srcRoot
        startDate = (endDate - datetime.timedelta(1))
        startTime = -1
        endTime = -1
        try:
            hours = os.listdir(os.path.join(srcRoot,'client11_Rogers','success',startDate.strftime('%Y-%m-%d')))
            for i in range(len(hours)):
                if len(hours) == 1:
                    startTime = hours[0]
                if float(hours[i])-float(hours[i-1]) > 1:
                    startTime = hours[i]
                    break
        except(FileNotFoundError):
            print('folder',startDate,'does not exist!\
                    Workday starts on',endDate)
        hours = os.listdir(os.path.join(srcRoot,'client11_Rogers','success',endDate.strftime('%Y-%m-%d')))
        if startTime == -1:
            startDate = endDate
            startTime = hours[0]
        endTime = hours[-1]
        startDateTime = datetime.datetime(startDate.year,startDate.month,startDate.day,int(startTime[:-3]))
        endDateTime = datetime.datetime(endDate.year,endDate.month,endDate.day,int(endTime[:-3]))
        return startDateTime,endDateTime

    def trpWalk(self,backup=False):
        startTime = self.startDateTime.hour
        startDate = self.startDateTime.strftime('%Y-%m-%d')
        endDate = self.endDateTime.strftime('%Y-%m-%d')
        srcRoot = self.srcRoot
        trpCollection = []
        if backup:
            startDate = self.date.strftime('%Y-%m-%d')
            endDate = startDate
            startTime = 0

        for root, dirs, files in os.walk(srcRoot):
            if endDate in dirs:
                dirs.clear()
                if startDate != endDate:
                    dirs.append(startDate)
                dirs.append(endDate)
            if len(dirs) > 0 and dirs[0].endswith('.00'):
                    while startDate in root and int(dirs[0][:-3]) < startTime:
                        print(dirs)
                        dirs.pop(0)
                    
            aList = []
            for name in files:
                if not name.endswith('.trp'):               
                    aList.append(name)
                while len(aList)>0:
                    files.remove(aList[0])
                    aList.pop(0)
            self.trpTripleRandomize(root,files,trpCollection)   
        return trpCollection
     
    def trpTripleRandomize(self,src,srcFiles,collector):
        i = 0        
        while(i < 3):
            try:
                randomFile = os.path.join(src,choice(srcFiles))
                if randomFile not in collector:
                    collector.append(randomFile)
                    #print(randomFile)
                    i += 1
                if len(srcFiles) < 3:
                    i += 1

            except(IndexError):
                break #in case of an empty list, choice() will fail

##########################SHELL COMMAND METHODS##############################

    def createDst(self):
        print('creating destination folder at',self.dstRoot)
        os.mkdir(self.dstRoot)
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
            print('copying',os.path.split(src)[1],'to',self.dstRoot)
            shutil.copy(src,self.dstRoot)
        print('Files successfully copied!')

    def __repr__(self):
        aStr = '.trp file dump from ' +\
               self.startDateTime.strftime('%Y-%m-%d %H.00') +\
               ' until ' +\
               self.endDateTime.strftime('%Y-%m-%d %H.00')
        return aStr
