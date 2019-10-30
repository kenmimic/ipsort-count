#!/usr/bin/python

import sys,re,os.path,datetime

# add timestamp to file name function
def add_timestamp_function():
   return "IPCount-"+ str(datetime.datetime.now())+".txt"
parsed_ip=add_timestamp_function()
path="./"+parsed_ip

# check sys arguments and set up logfile with threshold
try:
    if sys.argv[2:]:
       logfile=sys.argv[1]
       threshold=int(sys.argv[2])
    else:
       logfile=raw_input("Enter absoulte path and threshold,e.g./var/log/apaches2/access.log 50")
       threshold=int(sys.argv[2])
# iterate ips array and parse logfile
    try:
       ips=[]
       file=open(logfile,"r")
       for text in file.readlines():
	   text = text.rstrip()
           found = re.findall(r'(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})',text)
	   if found:
	      ips.extend(found)
# save ips to outfile and print threshold
       outfile=open(path,"a")
       for count,address in sorted(((ips.count(e),e) for e in set(ips)),reverse=True):
	   outfile.write("%s has %d hits" %(address,count))
	   outfile.write("\n")
	   if count > threshold:
		print"%s has %d hits" %(address,count)

    finally:
       file.close()
       outfile.close()
except IOError,(errno,sterrno):
    print"I/O Error %s %s" %(error,sterror)
