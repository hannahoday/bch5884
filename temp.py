#!/usr/bin/env python3

#The link to my github repository is: https://github.com/hannahoday/bch5884.

f=int(input("Please enter fahrenheit degrees as an integer: "))
k=((f - 32) * 5) / 9 + 273.15

print("The temperature in Kelvin rounded to two decimal places is: ", round(k,2))
