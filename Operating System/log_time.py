import os
import datetime


def log_time():

        x = datetime.datetime.now()
        #..
        dt_now = str(x.year) +  str(x.month).zfill(2) + str(x.day).zfill(2) + str(x.hour).zfill(2) + str(x.minute).zfill(2) + str(x.second).zfill(2)
        print(dt_now)
        
        # 2021/04/12 13:56:47
        # dt_now = str(x.year) + '/' + str(x.month).zfill(2) + '/' + str(x.day).zfill(2) + ' ' + str(x.hour).zfill(2) + ':'  +str(x.minute).zfill(2) + ':' +str(x.second).zfill(2)

        # Open File
        f = open("/opt/py/output.txt", "a")

        # Write time to file
        f.write(dt_now)
        f.write("\n")

        f.close()
        
        

if(1):
        log_time()

