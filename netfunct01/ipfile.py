#!/usr/bin/env python3
def createIPList():
    theFile = open('work3.txt','r')
    theDict = {}
    fileLines = theFile.readlines()
    n = 0
    i = 0
    for i in range(len(fileLines)):
        theDict[fileLines[i]] = fileLines[n]
        #n += 1
    print(theDict)

createIPList()