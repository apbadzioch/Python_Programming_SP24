print("# print $ symbol 10 times using while loop in a single line: $$$$$$$$$$")
i = 0
while i < 10:
  print('$', end = '')
  i += 1
print()
print()
    
print("# display multiples of 7 from 7 to 70:")
i = 7
while i <= 70:
  print(i)
  i += 7
print()

for i in range(7, 71, 7):
    print(i, end = ' ')
print()
print()
      

print("# display odd numbers from 30 to 50 horizontally: ")
for i in range(30, 51):
    if i % 2 == 1:
      print(i, end = ' ')
print()
print()

print("# display cube of numbers 1-5")
for i in range(1, 6):
      #print(i, i ** 3)
    print(i, pow(i, 3))
print()

print("# display sum of numbers 1-5")
i = 1
t = 0
while i <= 5:
  t += i
  i += 1
print(t)
print()

print("# display count of lowercase alphabets in a string PYthon.py:")
c = 0
s = "PYthon.py"
for e in s:
  if e.islower():
    c += 1
print(c)
print()

print("# read characters repeatedly until Q/q is entered and display the number of characters entered:")
i = 0
ch = input ("Enter a character: ")
# while ch != 'Q' or ch != 'q':
while ch.upper() != 'Q':            # ch.lower() != 'q': 
  ch = input ("Enter a character: ")
  i += 1
print(i)
print()

print("# repeatedly input a score until the score between 0-100 is entered:")
score = int(input ("Enter a score: "))
while score < 0 or score > 100: 
  score = int(input ("Enter a score: "))
print()

print("# display factorial of 5 is  factTotal = 1 * 2 * 3 * 4 * 5:")
factTotal = 1
for i in range(1, 6):
    factTotal *= i
print(factTotal)
print()

