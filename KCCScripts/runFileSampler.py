from RandomFileSampler1_0 import FileSampler
import datetime

srcRoot = 'C:\\Users\\Nathan\\Desktop\\fileSamplerPG\\sample_root'
dstRoot = 'C:\\Users\\Nathan\\Desktop\\fileSamplerPG\\destination_root'
date = datetime.date.today()
##date = datetime.date(2019,6,5)##remove '##' to manually enter date!


print('Collecting .trp files...')
a = FileSampler(srcRoot,dstRoot,date)
print('.trp files found!')
a.dump()
