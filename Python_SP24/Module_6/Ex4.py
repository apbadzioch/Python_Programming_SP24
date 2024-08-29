# Topics
'''
- Index Operator ([n])
- Slicing Operator ([start:end])
'''

# program description
'''
Receive the user's full name.
Find and print the user's first and last character of the name using indexing and slicing.
Print user's first name using indexing and slicing
Print user's last name using indexing and slicing
Print user's middle initial using indexing and slicing
Print the user's name in the format using slicing: Last, First Middle.
    For example: if my name is Suma V. Rao then it should print rao, suma v.
'''

name = input("enter name: ") # suma v. rao
ln = len(name)

print("21", name[0])
print("22", name[ln-1])     # name[-1]

print("24", name[0:1])       # name [0:1]
print("25", name[-1:ln])

print("27 " + name[0]+name[1]+name[2]+name[3])
print("28 " + name[:4])

print("30 " + name[-3]+name[-2]+name[-1])
print("31 " + name[-3:len(name)]) # name[-3:]

fname = name[:4]
lname = name[-3:]
mi = name[-6:-4]
print(lname + ", " + fname, mi)






    
