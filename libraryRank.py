# [{'book' : [ ], 'sign' : X , 'ship' :   Y }, ..............          ]
# Formula used is (book score * books shippable per day) / (days taken to sign up library)
#from bookBooking import *
# scores, bookFlag, library 
library = [{'sign': 2, 'ship': 2, 'books': [0, 1, 2, 3, 4]}, {'sign': 3, 'ship': 1, 'books': [0, 2, 3, 5]}]
scores =  [1, 2, 3, 6 , 5, 4]
bookFlag = [False, False, False, False, False, False]
score = 0
days = 1
parameter = 0
highest = 0
index = 0
flagCopy = bookFlag
i = 0

# Initial calculation of scores for each library when no books have scanned
for i in range(0, 1):
    for lib in library: 
        days = lib['sign']
        for book in lib['books']:
            if flagCopy[book] == False:
                score += scores[book]
                flagCopy[book] = True
        score = score/lib['ship'] + score % lib['ship']
        score /= days
    if score > highest:
        highest = score
        index = lib
    score = 0
    days = 1
    
#SelectLibrary(index) 
flagCopy = bookFlag 
# Parameter can be fine tuned based on experimentation 
parameter = 3
while True:
    for lib in library: 
        days = lib['sign']
        for book in lib['books']:
            if flagCopy[book] == False:
                score += scores[book]
                flagCopy[book] = True
        score = score/lib['ship'] + score % lib['ship']
        score /= days
    if score >= parameter:
        #SelectLibrary(lib)
        bookFlag = flagCopy
    score = 0
    flagCopy = bookFlag


