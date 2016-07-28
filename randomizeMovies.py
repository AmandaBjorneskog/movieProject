#!/usr/bin/python

import sys
import random
import linecache

filename = "movies.txt"
arr = []
nrOfLines = 0
randomNr = 0

with open(filename) as myFile:
    for num, line in enumerate(myFile,1):
        nrOfLines = nrOfLines +1

with open(filename) as f:
    arr = f.readlines()
    
randomNr = random.randint(1,(nrOfLines-1))

print(arr[randomNr])
               
    
for i in range(randomNr, nrOfLines-1):
    arr[i] =  arr[i+1]

with open(filename, 'w') as file:
    file.writelines(arr)
