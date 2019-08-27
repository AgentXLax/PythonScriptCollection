from playground import FileSampler
import datetime

srcRoot = 'D:\\Backup\\23610009_CUS_Rogers_Network_Optimization_Program\\CA_Campaign_02\\System2\\Raw_Data'
dstRoot = 'D:\\BUDump'

date = datetime.date(2019,8,23)


print('Collecting .trp files...')
a = FileSampler(srcRoot,dstRoot,date,backup=True)
print('.trp files found!')
a.dump()
