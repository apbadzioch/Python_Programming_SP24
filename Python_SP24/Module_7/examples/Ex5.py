# nested loops

'''
Have the user enter 3 inputs: any character, in how many rows to print, and
in how many columns.  Then, display in the following pattern using nested loops

For example:
Enter a character to print: $
In how many rows? 3
In how many columns? 4
$$$$
$$$$
$$$$
'''
LINE = '~' * 10

# using nested for loops
sym = input("Enter a character to print: ")
rows = int(input("In how many rows? "))
cols = int(input("In how many cols? "))

for r in range(rows):
    for c in range(cols):
        print(sym, end = '')
    print()
print(LINE)

# using nested while loops
r = 0
while r < rows:
    c = 0
    while c < cols:
        print(sym, end = '')
        c += 1
    r += 1
    print()
print(LINE)

# using combo loops
for r in range(rows):
    c = 0
    while c < cols:
        print(sym, end = '')
        c += 1
    print()
print(LINE)

# using combo loops
r = 0
while r < rows:
    for c in range(cols):
        print(sym, end = '')
    r += 1
    print()
print(LINE)
