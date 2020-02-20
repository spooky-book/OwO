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

# Initial calculation of scores for each library when no books have scanned
for i in range(0, 1):
    for lib in library: 
        days = lib['sign']
        score = lib['ship']
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
                score += 1
                flagCopy[book] = True
        score =/ days
        score *= lib['ship']
    if score >= parameter:
        SelectLibrary(lib)
        bookFlag = flagCopy
    score = 0
    flagCopy = bookFlag


