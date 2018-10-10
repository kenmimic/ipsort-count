#!/usr/bin/python
from optparse import OptionParser
import re,sys,os.path
#check input sys.argv[]
try:
    if sys.argv[2:]:
        print"File parsed %s"%(sys.argv[1])
        logfile=sys.argv[1]
        threshold=int(sys.argv[2])
    else:
        logfile=raw_input("Enter log and threshold to parse,e.g./var/log/apache2/access_log 100 ")
        threshold=int(sys.argv[2])
# open file to parse, sort and store in ips[]
    try:
        ips=[]
        file=open(logfile,"r")
        for text in file.readlines():
            text = text.rstrip()
            found = re.findall(r'(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})',text)
            if found:
                ips.extend(found)
        outfile=open("./IPCount","a")
        for count,address in sorted(((ips.count(e),e) for e in set(ips)),reverse=True):
            outfile.write("%s has %d hits" %(address,count))
            outfile.write("\n")
            if count > threshold:
                print("%s has %d hits" %(address,count))
    finally:        
        file.close()
        outfile.close()
except IOError,(errno,sterrno):
    print"I/O Error %s %s"%(error,strerror)
