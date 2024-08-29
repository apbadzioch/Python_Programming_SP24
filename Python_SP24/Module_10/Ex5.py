# List comprehension: concise syntax in creating a new list from an existing list
'''
Using functions do the following:
Create, initialize, and print a courses list with  the following courses offered:
    ["COSC1436", "cosc1437", "COSC2425", "COSC2436", "ITSE2410", "ITSE2473", "INEW2332", "INEW2434"]
Based on the above course list, create and print a new list with only COSC courses and then only ITSE and INEW courses

Example:
['COSC1436', 'coSC1437', 'cosc2425', 'Cosc2436', 'itse2410', 'ITSE2473', 'Inew2332', 'INEW2434']
['COSC1436', 'COSC1437', 'COSC2425', 'COSC2436', 'ITSE2410', 'ITSE2473', 'INEW2332', 'INEW2434']
['COSC1436', 'COSC1437', 'COSC2425', 'COSC2436']
['ITSE2410', 'ITSE2473']
'''

COURSES = ['COSC1436', 'coSC1437', 'cosc2425', 'Cosc2436', 'itse2410', 'ITSE2473', 'Inew2332', 'INEW2434']

def convertUp(coursesUp):
    for i in COURSES:
        coursesUp.append(i.upper())

def findCosc(coursesUp, coursesCosc):
    for i in coursesUp:
        if "COSC" in i:
            coursesCosc.append(i)

def findItse(coursesUp):
    return [i for i in coursesUp if "ITSE" in i]

def findInew(coursesUp):
    return [i for i in coursesUp if "INEW" in i]

def main():
    print(COURSES)

    coursesUp = []
    convertUp(coursesUp)
    print(coursesUp)

    coursesCosc = []
    findCosc(coursesUp, coursesCosc)
    print(coursesCosc)

    coursesItse = findItse(coursesUp)
    print(coursesItse)

    coursesInew = findInew(coursesUp)
    print(coursesInew)

main()

# OUTPUT
'''
['COSC1436', 'coSC1437', 'cosc2425', 'Cosc2436', 'itse2410', 'ITSE2473', 'Inew2332', 'INEW2434']
['COSC1436', 'COSC1437', 'COSC2425', 'COSC2436', 'ITSE2410', 'ITSE2473', 'INEW2332', 'INEW2434']
['COSC1436', 'COSC1437', 'COSC2425', 'COSC2436']
['ITSE2410', 'ITSE2473']
['INEW2332', 'INEW2434']
'''
