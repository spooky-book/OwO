def getOutput(outputData):
    outputFD = open("bookings.txt", "w+")
    outputFD.write(str(len(outputData)) + "\n")
    for schedule in outputData:
        outputFD.write(str(schedule["lib_id"]) + " " + str(schedule["amount"] ) + "\n")
        outputFD.write(' '.join(str(i) for i in schedule["book_ids"]) + "\n")

#Read File
inputFile = sys.argv[1]+".txt"
inputFD = open(inputFile, "r+")

properties = [int(i) for i in inputFD.readline().split()]
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

    output =  []

#Process Schedules
currentTime = 0
#loops through time till no more time
#you have to add a way to increment time
while currentTime <= daysTotal:
    #library = getBestLibrary(sortedData)
    # you have to add a way to select the correct library here 
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

    #add books here
                #lib_sch["amount"] += 1
                #lib_sch["book_ids"].append(searchId)
                #every time you add a book put the above code

    #increment time by some value
    #currentTime += library["sign"]

getOutput(output)