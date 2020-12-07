#!/usr/bin/env python3

#bch5884 final project code
#author Hannah O'Day
#uploaded to github repository: https://github.com/hannahoday/bch5884.git

import numpy as np
import matplotlib.pyplot as plt
import math
from mpl_toolkits import mplot3d
from scipy import signal


#parse lines read from SIMION file into x,y,z
#returns 1D arrays x[],y[],z[]
def parse(lines):
    for line in lines[10:800]:
        words=line.split(')')
        for word in words:              #Looking for keywords "X","Y","Z"
            if "X" in word:
                xp=word.split('(')
                xc=xp[1].split()
                xcoor=xc[0]
                x.append(xcoor)
            if "Y" in word:
                yp=word.split('(')
                yc=yp[1].split()
                ycoor=yc[0]
                y.append(ycoor)
            if "Z" in word:
                zp=word.split('(')
                zc=zp[1].split()
                zcoor=zc[0]
                z.append(zcoor)
    return(x,y,z)

#plotting 3D trajectory
#saves plot to "trajectory.png"
def trajectory(xline,yline,zline):
    fig1=plt.figure()
    ax=plt.axes(projection='3d')
    ax.plot3D(xline,yline,zline)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Ion Trajectory')
    plt.savefig("trajectory.png")
    
#converting to cylinderical coordinates
#returns r conversion when i = x, j = y coordinates
def convert_r(i,j):
    return math.sqrt(i**2+j**2)
#returns phi conversion when i = x, j = y coordinates
def convert_phi(i,j):
    return math.atan(j/i)
    
#create new text file "coor.txt" of just x, y, z coordinates
def newcoorfile(x,y,z):
    newf=open("coor.txt","w")
    for i in range(len(x)):
        newf.write(x[i] + " " + y[i] + " " + z[i]+ "\n")
    newf.close   

#writes html website code "FinalProject.html", using figures produced in code  
def website(fig1,fig2,fig3):
    newfile=open("FinalProject.html","w")
    newfile.write("<!DOCTYPE html>\n<html>\n<head>\n<title>Final Project</title>\n</head>\n<style>\nbody {background-color: powderblue;}\n img{border-radius:5px}\n h1{color: #000080; font-size:300%}\ntable {font-size:150%}\np{font-size:150%}\n</style>\n<h1 style=\"font-family:verdana\">Final Project: Plotting Ion Trajectories from SIMION</h1>\n<table style = \"width:90%\" >\n<tr><td style=\"font-family:verdana\">In the Bleiholder Lab, I have been studying ion trajectories in our trapped ion mobility spectrometry (TIMS) instrument. To study ion trajectories, I have been using SIMION, an ion optics simulation program that simulates ion trajectories based on user defined electric potentials. The image to the right is an example of a 3D ion trajectory collected from a qudrupole ion trap simulation produced by SIMION. Any ion trajectory produced from SIMION can be graphed similarly to this, with the following power specrtal analysis on different frequency components in the trajectory.</td><td><img src=\"trajectory.png\"></td></tr><tr><th style=\"font-family:verdana\">Ion Trajectory in the r-Direction (Green) and the Power Spectral Density (Blue)</th><th style=\"font-family:verdana\">Ion Trajectory in the z-Direction (Green) and the Power Spectral Density (Blue)</th></tr><tr><td align=\"center\"><img src=\"psdr.png\"></td><td><img src=\"psdz.png\"></td></tr></table><p style=\"font-family:verdana\"> These power spectral densities (PSDs) can be used to examine the contribution of different frequency components to the ion trajectory. What should be noticed here is that there are clearly more frequencies in the r-direction than the z-direction. So, in this example of a quadrupole ion trap, ions experience more types of motion in the radial direction than the axial. In the future, more simulations will be run in SIMION to further show differences in axial and radial contributions in ion trajectories.")
    newfile.close

#performs power spectral density of 1D array
#data is the signal to perform psd on
#creates plots of trajectories and psd side by side
def psd(data):
    fs=1e3
    f, Pxx_den = signal.welch(data,fs)
    plt.subplot(211)
    plt.plot(data, 'g-')
    plt.subplot(212)
    plt.plot(f, Pxx_den)
    plt.xlabel('Frequency')
    plt.ylabel('Power')
    plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))

#print statement when running file
print("This program takes ion trajectory data from SIMION and plots it in 3D. \nThen, a PSD is performed on the r and z directions of the trajectory")

#reading file
f=open("trapdata.txt")
lines=f.readlines()
f.close()

#set x,y,z arrays
x=[]
y=[]
z=[]

#call parse function
parse(lines)

#need to make sure arrays are float
xline=np.array(x)
xline=np.asfarray(xline,float)
yline=np.array(y)
yline=np.asfarray(yline,float)
zline=np.array(z)
zline=np.asfarray(zline,float)

#plot trajectory, calling trajectory function
trajectory(xline,yline,zline)

#declare r and phi arrays
r=[]
phi=[]

#use convert_phi and convert_r functions to get cylindrical coordinates
#uses for loop to add to r and phi arrays
for i in range(len(xline)):
    r.append(convert_r(xline[i],yline[i]))
    phi.append(convert_phi(xline[i],yline[i]))

#call psd function for z direction
fig3=psd(zline)
#save image as "psdz.png"
plt.savefig("psdz.png")
#close all plots
plt.close()

#call psd function in r direction
fig4=psd(r)
#save image as "psdr.png"
plt.savefig("psdr.png")

#call website making function with pictures produced in code: "trajectory.png", "psdr.png", "psdz.png" 
website("trajectory.png","psdr.png","psdz.png")

#make new coordinate file "coor.txt" for future reference
newcoorfile(x,y,z)

#Prints done statement
print("Done")