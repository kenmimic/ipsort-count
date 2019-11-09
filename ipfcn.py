#!/usr/bin/python

import argparse,sys,os.path,re,datetime

# add timestamp to file name function
def add_timestamp_filename():
   return "IPCount-"+str(datetime.datetime.now())+".txt"
parsed_ip=add_timestamp_filename()
path="./"+parsed_ip
# check sys.argv use and argparse

parser = argparse.ArgumentParser()
parser.add_argument("-v", action="count", default=0)
parser.add_argument("logPath", help="Enter absolute path e.g./var/log/syslog")
parser.add_argument("threshold",type=int, help="hit threshold e.g. 100")
args = parser.parse_args()

try:
   if sys.argv >= 1:
      logfile=sys.argv[1]
      threshold=int(sys.argv[2])
   else:
      sys.exit(1)
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
