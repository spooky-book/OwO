# [{'book' : [ ], 'sign' : X , 'ship' :   Y }, ..............          ]
from bookBooking import *
# scores, bookFlag, library 
score = 0
delay = 1
parameter = 0
highest = 0
i = 0
for i in range(0, 1):
    for lib in library: 
        delay *= lib['sign']
        for book in lib['book']:
            if bookFlag[book] == False:
                score += 1
                bookFlag[book] = True
        delay *= lib['ship'] 
        score =/ delay
    if score > highest:
        highest = score
    score = 0
    delay = 1

