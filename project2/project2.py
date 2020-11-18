#!/usr/bin/env python3

#bch5884 project2 code
#author Hannah O'Day
#uploaded to github repository: https://github.com/hannahoday/bch5884.git

import numpy
from matplotlib import pyplot
import math

#reading file
f=open("superose6_50.asc")
lines=f.readlines()
f.close()

#setting array variables
t=[]
a=[]

#parsing file into arrays t[] and a[]
for line in lines[3:]:
    words=line.split()
    try:
        t.append(float(words[0]))
        a.append(float(words[1]))
    except:
        print("could not parse", line)
        continue

#converting to numpy
t=numpy.array(t)
a=numpy.array(a)

#taking gradient of array a[]
da=numpy.gradient(a)

#setting arrays for peak[][] = peak maximums, peakend[][] = peak endings, peakbeg[][] = peak beginnings
peak=[[],[]]
peakend=[[],[]]
peakbeg=[[],[]]

#setting count for for loop
count=300

#truncated the data from points 300-627
for i in da[300:627]:
    #finding peaks by looking for where the derivative is 0 (or passes through it)
    boo=da[count]>0 and da[count+1]<0
    if boo==True:
        peak[0].append(t[count])
        peak[1].append(a[count])
    #finding peak end by looking at where the derivative goes from negative to positive
    boo2=da[count]<=0 and da[count+1]>=0
    if boo2==True:
        peakend[0].append(t[count])
        peakend[1].append(a[count]) 
    #finding peak beginning by looking at rate of increase in derivative
    boo3=da[count]<=0.1 and da[count+1]>=0.11
    if a[count+1]-a[count]>1 and a[count+1]-a[count]<1.11:
        peakbeg[0].append(t[count])
        peakbeg[1].append(a[count])         
    if count<879:
        count=count+1


#printing statement for peak maximums and delineation of peaks
print("The peak maximums (time, maximum) are located at:\n(",peak[0][0],",",peak[1][0],"), (",peak[0][1],",",peak[1][1],"), (",peak[0][2],",",peak[1][2],"), and (",peak[0][3],",",peak[1][3],")")
print("Peak 1 begins at time ",peakbeg[0][0]," and ends at time ",peakend[0][0])
print("Peak 2 begins at time ",peakbeg[0][1]," and ends at time ",peakend[0][1])
print("Peak 3 begins at time ",peakbeg[0][2]," and ends at time ",peakend[0][2])
print("Peak 4 begins at time ",peakbeg[0][3]," and ends at time ",peakend[0][3])

#plotting graph with all points and legend
pyplot.plot(t,a)
peakmax, = pyplot.plot(peak[0],peak[1],'ro',label='Peak Max')
endpeak, = pyplot.plot(peakend[0],peakend[1],'bs', label='Peak End')
begpeak, = pyplot.plot(peakbeg[0],peakbeg[1],'k^', label='Peak Beginning')
pyplot.legend(handles=[peakmax, endpeak, begpeak])

#saving plot to 'project2.png'
pyplot.savefig("project2.png")

#show plot
pyplot.show()