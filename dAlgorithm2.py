#!/usr/bin/python
import sys
#arg value is a_example, b_small, c_medium etc

books = 0 
libraries = None 
daysTotal = None
scores = None
data = []
seen = []

def get_Stuff():
    # inputFile = "a_example.txt"
    inputFile = "b_read_on.txt"
    inputFD = open(inputFile, "r+")

    properties = [int(i) for i in inputFD.readline().split()]
    print (properties)

    global books
    books = properties[0]
    global libraries 
    libraries = properties[1]
    global daysTotal 
    daysTotal = properties[2]
    global scores
    scores = [int(i) for i in inputFD.readline().split()]

    for i in range(libraries):
        libraryProp = [int(i) for i in inputFD.readline().split()]
        libraryBook = [int(i) for i in inputFD.readline().split()]
        library = {
            "sign": libraryProp[1],
            "ship": libraryProp[2],
            "books": libraryBook,
            "id": i
        }
        data.append(library)

    # print(scores)
    # print (data)



def find_unique_score():
    unique_score = []
    global data
    for i in range(len(data)):
        library = data[i]
        lib_score = 0
        for book in library['books']:
            temp_seen = list(seen)
            unseen_books = 0
            if temp_seen[book] == False:
                lib_score += scores[book]
                temp_seen[book] == True
                unseen_books += 1
        lib_score /= unseen_books   #average score pre unseen book
        lib_score /= library['sign']    #average score per unseen book per day
        lib_score *= library['ship']

        unique_score.append([lib_score, i])

    unique_score.sort(key = lambda x: x[0], reverse=True)
    print("UNIQUE SCORE", unique_score)

    return unique_score

def main():
    get_Stuff()
    global seen
    global data
    for i in range(books):
        seen.append(False)

    print("bruh")

    dayCount = 0
    
    timeline = []

    while dayCount < daysTotal and len(data) > 0:
        unique_score = find_unique_score()
        print("unique score: ", unique_score)

        chosen = data.pop(unique_score[0][1])

        timeline.append([chosen, dayCount, unique_score[0][1]])

        for book in chosen['books']:
            seen[book] == True

        print(chosen['sign'])
        dayCount += chosen['sign']

    print("timeline: ", timeline)

    output(timeline)

    
def output(timeline):
    global daysTotal
    try:
        output_file = open('1.out', 'w')
    except:
        exit(1)
    
    
    output_file.write(str(len(timeline)))    #libraries signed up
    output_file.write('\n')
    for library in timeline:
        output_file.write(str(library[0]['id']) + ' ')
        small = min((daysTotal - library[1]) * library[0]['ship'], len(library[0]['books']))
        output_file.write(str((small)))
        output_file.write('\n')
        for book in library[0]['books']:
            output_file.write(str(book) + ' ')
            if small == 0:
                break
            small -=1
            
        # output_file.write(library[0]['books'])  #can be better
        output_file.write('\n')
        
        

def pointCalculate():
    pass

if __name__ == "__main__":
    main()