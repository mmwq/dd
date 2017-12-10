#!/usr/bin/python
# -*- coding: UTF-8 -*-

# import sys
import time
import os

# def trace(data):
data_read = open("data.txt")
data_list = data_read.readlines()
print data_list.__len__()
for line in data_list:
    _time = line.strip().split(",")[1]
# print _time
    time_local = time.localtime(int(_time))
# print time_local
    dt = time.strftime("%Y%m%d", time_local)
    data_write = open(dt, "a")
    data_write.write(line)
print "end"


# if __name__ == "__main__":
#     data = sys.argv[1]
#     trace(data)
