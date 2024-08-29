# List comprehension: concise syntax in creating a new list from an existing list
'''Using functions fo the follonwing:
Create, initialize, and print a course list with the following courses offered:
    ["COSC1436", "COSC1437", "COSC2425", "COSC2435", "COSC2436", "ITSE2410", "ITSE2473", "INEW2332", "INEW2434"]
Based on the above course list, create and print a new list with only COSC courses and then only ITSE courses.
'''


COURSES = ["COSC1436", "coSC1437", "cosc2425", "Cosc2435", "COSC2436", "itse2410", "ITSE2473", "Inew2332", "INEW2434"]

def convertUp(courseUp):
    for i in COURSES:
        courseUp.append(i.upper())

def findCosc(courseUp, courseCosc):
    for i in courseUp:
        if "COSC" in i:
            courseCosc.append(i)

def findItse(courseUp):
    return [i for i in courseUp if "ITSE" in i]

def findInew(courseUp):
    return [i for i in courseUp if "INEW" in i]


def main():
    print(COURSES)

    courseUp = []
    convertUp(courseUp)
    print(courseUp)
    
    courseCosc = []
    findCosc(courseUp, courseCosc)
    print(courseCosc)

    courseItse = findItse(courseUp)
    print(courseItse)

    courseInew = findInew(courseUp)
    print(courseInew)

main()