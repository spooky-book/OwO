# [{'book' : [ ], 'sign' : X , 'ship' :   Y }, ..............          ]
from bookBooking import *
# scores, bookFlag, library 
score = 0
days = 1
parameter = 0
highest = 0
index = 0
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
# Parameter can be optimised later on 
parameter = 10
while True:
    for lib in library: 
        days = lib['sign']
        for book in lib['book']:
            if bookFlag[book] == False:
                score += 1
                bookFlag[book] = True
        days *= lib['ship'] 
        score =/ delay
    if score > parameter:
        parameter = score
    score = 0


