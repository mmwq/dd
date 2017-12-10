#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import matplotlib.pyplot as plt


folderPath = os.path.dirname(os.path.realpath(__file__)) + "\day"
# print folderPath
fileList = os.listdir(folderPath)
# plt.ylabel('some numbers')

# for fileName in fileList:
file = open("C:\Users\\54959\Documents\VScode\python\didi\day\\20170505")
linesList = file.readlines()
x = []
y = []
for line in linesList:
    x.append(line.split(",")[2])
    y.append(line.split(",")[3])
# plt.plot(x, y, 'r,')
plt.axis([520000,524000,53000,59000])
ax = plt.gca()
ax.set_aspect(1)

plt.plot([521677,521580,521520,521452,521433,521411,521400],[58109,57466,57059,56668,55855,54822,53998],'b')
plt.plot(x,y,'ro')

fig = plt.gcf()
fig.savefig('20170505.png', dpi=500)
plt.show()
