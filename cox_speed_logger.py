import os
import sys
import csv
import datetime
import time
import subprocess



def test():

        #run speedtest-cli
        output = open('coxresults.csv', 'a')
        print("running test")
        a = subprocess.Popen('speedtest-cli', stdout = output)
        timeoflog = [datetime.datetime.now()]
        w = csv.writer(output)
        w.writerow(timeoflog)






if __name__ == '__main__':
        test()
        print("completed")
