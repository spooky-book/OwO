#!/usr/bin/python
import sys
#arg value is a_example, b_small, c_medium etc
def grabbingData(fileName):
    inputFile = fileName + ".txt"
    inputFD = open(inputFile, "r+")

    properties = [int(i) for i in inputFD.readline().split()]
    print (properties)
    books, libraries, daysTotal = properties

    scores = [int(i) for i in inputFD.readline().split()]

    data = []


    for i in range(libraries):
        libraryProp = [int(i) for i in inputFD.readline().split()]
        libraryBook = [int(i) for i in inputFD.readline().split()]
        library = {
            "sign": libraryProp[1],
            "ship": libraryProp[2],
            "books": libraryBook
        }
        data.append(library)

    print (data)