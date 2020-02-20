#!/usr/bin/python
import sys
#arg value is a_example, b_small, c_medium etc


def getBestLibrary(sortedData):
    for library in sortedData:
        if library["booksLeft"] > 0:
            return library

def getOutput(outputData):
    outputFD = open("bookings.txt", "w+")
    outputFD.write(str(len(outputData)) + "\n")
    for schedule in outputData:
        outputFD.write(str(schedule["lib_id"]) + " " + str(schedule["amount"] ) + "\n")
        outputFD.write(' '.join(str(i) for i in schedule["book_ids"]) + "\n")







inputFile = sys.argv[1]+".txt"
inputFD = open(inputFile, "r+")

properties = [int(i) for i in inputFD.readline().split()]
#print (properties)
books, libraries, daysTotal = properties

bookFlag = [False] * books

bookCount = []
for i in range(books):
    book = {
        "id": i,
        "no": 0
    }
    bookCount.append(book)

scores = [int(i) for i in inputFD.readline().split()]

data = []


for i in range(libraries):
    libraryProp = [int(i) for i in inputFD.readline().split()]
    libraryBook = [int(i) for i in inputFD.readline().split()]
    library = {
        "id": i,
        "booksLeft": libraryProp[0],
        "sign": libraryProp[1],
        "ship": libraryProp[2],
        "books": libraryBook
    }
    for bookID in library["books"]:
        bookCount[bookID]["no"] += 1
    data.append(library)

bookCount = sorted (bookCount, key=lambda k: k["no"])
#print (bookCount)

sortedData = sorted(data, key=lambda k: (k["sign"], len(k["books"])))
#print (sortedData)

output =  []


currentTime = 0
while currentTime <= daysTotal:
    library = getBestLibrary(sortedData)
    if not any(lib_sch["lib_id"] == library["id"] for lib_sch in output):
        lib_sch = {
            "lib_id": library["id"],
            "amount": 0,
            "book_ids": []
        }
        output.append(lib_sch)
    else:
        for lib_sch in output:
            if lib_sch["lib_id"] == library["id"]:
                break


    for ship in range(library["ship"]):
        for book in bookCount:
            searchId = book["id"]
            if bookFlag[searchId] == False and searchId in library["books"]:
                #print ("Book", searchId, "booked in library", library["id"])
                bookFlag[searchId] = True
                library["booksLeft"] -= 1
                lib_sch["amount"] += 1
                lib_sch["book_ids"].append(searchId)
                break
    currentTime += library["sign"]
    print (currentTime)

#print(output)

getOutput(output)
