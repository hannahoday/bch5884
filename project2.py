#!/usr/bin/env python3

#bch5884 project2 code
#author Hannah O'Day
#uploaded to github repository: https://github.com/hannahoday/bch5884.git

import numpy
from matplotlib import pyplot


f=open("superose6_50.asc")
lines=f.readlines()
f.close()

t=[]
a=[]

for line in lines[3:]:
    words=line.split()
    try:
        t.append(float(words[0]))
        a.append(float(words[1]))
    except:
        print("could not parse", line)
        continue


t=numpy.array(t)
a=numpy.array(a)

da=numpy.gradient(a)
dda=numpy.gradient(da)

pyplot.plot(t,a)
pyplot.show()