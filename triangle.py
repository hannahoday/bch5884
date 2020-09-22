#!/usr/bin/env python3
#The link for my github repository is: https://github.com/hannahoday/bch5884.

import math

print("This program will give the angles, in degrees, for a valid triangle defined by integer coordinates")
Ax=int(input("Insert x-coor of point A: "))
Ay=int(input("Insert y-coor of point A: "))
Bx=int(input("Insert x-coor of point B: "))
By=int(input("Insert y-coor of point B: "))
Cx=int(input("Insert x-coor of point C: "))
Cy=int(input("Insert y-coor of point c: "))

a=math.sqrt((Cx-Bx)**2+(Cy-By)**2)
b=math.sqrt((Cx-Ax)**2+(Cy-Ay)**2)
c=math.sqrt((Ax-Bx)**2+(Ay-By)**2)

if a==b :
    gamma=90
    alpha=45
    beta=45
elif b==c :
    alpha=90
    gamma=45
    beta=45
elif c==a :
    beta=90
    gamma=45
    alpha=45
else:
    alpha=int(round((math.acos(((b**2)+(c**2)-(a**2))/(2*b*c)))*(180/math.pi)))
    beta=int(round((math.acos(((a**2)+(c**2)-(b**2))/(2*a*b)))*(180/math.pi)))
    gamma=180-alpha-beta

print("alpha: ", alpha, " degrees")
print("beta: ", beta, " degrees")
print("gamma: ", gamma, " degrees")




