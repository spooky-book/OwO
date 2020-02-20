# [{'book' : [ ], 'sign' : X , 'ship' :   Y }, ..............          ]
# Formula used is (book score * books shippable per day) / (days taken to sign up library)
from bookBooking import *
# scores, bookFlag, library 
score = 0
days = 1
parameter = 0
highest = 0
index = 0
flagCopy = bookFLag
i = 0
exhausted = True

# Initial calculation of scores for each library when no books have scanned
for i in range(0, 1):
    for lib in library: 
        days = lib['sign']
        score = (len(lib['book']))/lib['ship'] + score % lib['ship']
        score =/ days
    if score > highest:
        highest = score
        index = lib
    score = 0
    days = 1
    
SelectLibrary(index) 
# Parameter can be fine tuned based on experimentation 
parameter = 5
while True:
    for lib in library: 
        days = lib['sign']
        for book in lib['book']:
            if flagCopy[book] == False:
                score += scores[book]
                flagCopy[book] = True
        score = score/lib['ship'] + score % lib['ship']
        score /= days
    if score >= parameter:
        SelectLibrary(lib)
        bookFlag = flagCopy
    score = 0
    flagCopy = bookFlag
    for elem in bookFlag:
        if elem == False:
            exhausted = False
    if exhausted:
        break
        


