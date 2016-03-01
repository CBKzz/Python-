"""
Columbia W4111 Intro to databases
Homework 2
"""

import sys
from collections import *

def load_data(file_path):
  import csv
  with file(file_path) as f:
    dialect = csv.Sniffer().sniff(f.read(2048))
    f.seek(0)
    reader = csv.reader(f, dialect)
    return [l for l in reader]


def q1(data):
  
 item=set()
 for index in range(len(data)):
	list=data[index]
	item.add(list[15])
 return len(item)-1

def q2(data):
 vendor=set()
 for index in range(len(data)):
 	list=data[index]
        vendor.add(list[13])
 return len(vendor)-1 
 

def q3(data):
 a=0
 b=0
 dic={}
 for i in range (1,len(data)):
        list=data[i]
        if list[2] in dic:
                a=dic[list[2]]
                dic[list[2]]=a+int(list[20])
        else: 
                dic[list[2]]=int(list[20])
 d={v:k for k,v in dic.items()}
 return d[max(d)]

def q4(data):
 a=0
 b=''
 for i in range (1,len(data)):
	list=data[i]
	if int(list[2])==2633:
		if int(list[20])>a:
			a=int(list[20])
			b=list[15]			
 return b

def q5(data):
 dic={}
 a=0
 for i in range (1,len(data)):
	list=data[i]
	if list[11]=='TEQUILA':
		if list[6] in dic:
			a=dic[list[6]]
			dic[list[6]]=a+int(list[20])
		else:
			dic[list[6]]=int(list[20])
 
 d={v:k for k,v in dic.items()}
 return d[max(d)]


if __name__ == '__main__':
  if len(sys.argv) != 2:
    sys.stderr.write("Usage: python hw2.py (path to input csv)\n")
    sys.exit(1)
  file_path = sys.argv[1]

  data=load_data(file_path)
  print q1(data)
  print q2(data)
  print q3(data)
  print q4(data)
  print q5(data)
