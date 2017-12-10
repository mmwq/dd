#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import sys


class Light:
    def __init__(self, _x, _y):
        self.x = _x
        self.y = _y

    def distance(self, _x, _y):
        return (self.x - _x)**2 + (self.y - _y)**2

    def direction(self, _x, _y):
        X = abs(self.x - _x)
        Y = abs(self.y - _y)
        if Y > X:
            if self.y < _y:
                return "a"
            else:
                return "b"
        else:
            if self.x > _x:
                return "c"
            else:
                return "d"


def trace(start_light, start_dire, end_light, end_dire, s):
    pre = str(start_light) + "_" + str(start_dire)
    suf = str(end_light) + "_" + str(end_dire)
    mid = ""
    if start_light == end_light:
        if start_dire == end_dire:
            return s
        s = pre + "->" + suf
        return s
    else:
        increment = 0
        if start_light < end_light:
            increment = 1
            b = "a"
            e = "b"
            if start_dire != "b":
                pre += "->" + str(start_light) + "_b"
            if end_dire != "a":
                suf = str(end_light) + "_a" + "->" + suf
        else:
            increment = -1
            b = "b"
            e = "a"
            if start_dire != "a":
                pre += "->" + str(start_light) + "_a"
            if end_dire != "b":
                suf = str(end_light) + "_b" + "->" + suf
        tmp_start = start_light
        tmp_end = end_light
        while tmp_start != tmp_end - increment:
            tmp_start += increment
            mid += str(tmp_start) + "_" + b + "->" + \
                str(tmp_start) + "_" + e + "->"
        s = pre + "->" + mid + suf
        return s


light_list = []
light_list.append(Light(521677, 58109))
light_list.append(Light(521580, 57466))
light_list.append(Light(521520, 57059))
light_list.append(Light(521452, 56668))
light_list.append(Light(521433, 55855))
light_list.append(Light(521411, 54822))
light_list.append(Light(521400, 53998))

fileName = "20170508.txt"
fileinPath = "C:\Users\\54959\Documents\VScode\python\didi\day\\"
fileoutpath = fileinPath + fileName.replace(".txt", "") + "\\"

directory = os.path.dirname(fileoutpath)
try:
    os.stat(directory)
except:
    os.mkdir(directory)       

filein = fileinPath + fileName
print filein
print fileoutpath

# exit

file = open(filein)
lines = file.readlines()
car_last = ""
car_line_dict = {}
for line in lines:
    car = line.split(",")[0]
    if car_line_dict.has_key(car):
        car_line_dict[car].append(line)
    else:
        tmp_list = []
        tmp_list.append(line)
        car_line_dict[car] = tmp_list

trace_dict = {}


for car, _lines in car_line_dict.items():
    start_light = -1
    end_light = -1
    start_dire = ""
    end_dire = ""

    firstline = _lines[0]
    start_x = float(firstline.split(",")[2])
    start_y = float(firstline.split(",")[3])
    distance_list = []
    for light in light_list:
        distance_list.append(light.distance(start_x, start_y))
    start_light = distance_list.index(min(distance_list))
    start_dire = light_list[start_light].direction(start_x, start_y)

    lastline = _lines[-1]
    end_x = float(lastline.split(",")[2])
    end_y = float(lastline.split(",")[3])
    distance_list = []
    for light in light_list:
        distance_list.append(light.distance(end_x, end_y))
    end_light = distance_list.index(min(distance_list))
    end_dire = light_list[end_light].direction(end_x, end_y)
    s_trace = ""
    s_trace = trace(start_light, start_dire, end_light, end_dire, s_trace)
    if s_trace == "":
        continue
    print car + "\t" + str(start_light) + "_" + start_dire + "\t" + str(end_light) + "_" + end_dire + "\t" + s_trace

    # if s_trace=="0_a->0_d":
    #     trace_list = s_trace.split("->")
    #     for i in range(len(trace_list)):
    #         if(i==0):
    #             continue
    #         pre_trace = trace_list[i-1]
    #         cur_trace = trace_list[i]
    #         tra = cur_trace.split("_")
    #         trb = pre_trace.split("_")
    #         if tra[0] == trb[0]:
    #             tmpkey = (trb[0] + trb[1] + "to" + tra[1]).strip()
    #             if trace_dict.has_key(tmpkey):
    #                 trace_dict[tmpkey].append(car+"\n")
    #             else:
    #                 tmp_list = []
    #                 tmp_list.append(car+"\n")
    #                 trace_dict[tmpkey] = tmp_list

    trace_list = s_trace.split("->")
    for i in range(len(trace_list)):
        if(i==0):
            continue
        pre_trace = trace_list[i-1]
        cur_trace = trace_list[i]
        tra = cur_trace.split("_")
        trb = pre_trace.split("_")
        if tra[0] == trb[0]:
            tmpkey = (trb[0] + trb[1] + "to" + tra[1]).strip()
            if trace_dict.has_key(tmpkey):
                trace_dict[tmpkey].append(car+"\n")
            else:
                tmp_list = []
                tmp_list.append(car+"\n")
                trace_dict[tmpkey] = tmp_list

for outname, items in trace_dict.items():
    fileOut = open(fileoutpath + outname, "w+")
    print fileoutpath + outname
    fileOut.write(str(len(items)) + "\n")
    fileOut.writelines(items)
    