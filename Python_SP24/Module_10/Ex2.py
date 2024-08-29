# List methods: append, insert, extend, sort, reverse, remove, clear, pop, index, count 

# Empty list
names = []

# append
names.append("simi")
names.append("su")
print("appended simi su", names)

# insert
names.insert(0, "stella")
print("inserted stella at the beginning", names)
names.insert(len(names), "suma")
print("inserted suma at the end", names)
             
# add a name to the end of the list
names.append("rao")
print("appended rao", names)

# extend
names1 = ["jim", "james"]
names.extend(names1)
print("extended with jim james", names)

# count
names2 = names1 * 3
print("names2 list", names2)
print("count of jim is =", names2.count("jim"))

# sort
names.sort()
print("sorted ascending names list using sort", names)

# reverse
names.reverse()
print("sorted descending names list using reverse", names)

# index
i = names.index("rao")
print("Index of rao", i)

# pop
names.pop(i)
print("After removing rao", names)

# clear
names.clear()
print("After clearing the list", names)

# OUTPUT
'''
appended simi su ['simi', 'su']
inserted stella at the beginning ['stella', 'simi', 'su']
inserted suma at the end ['stella', 'simi', 'su', 'suma']
appended rao ['stella', 'simi', 'su', 'suma', 'rao']
extended with jim james ['stella', 'simi', 'su', 'suma', 'rao', 'jim', 'james']
names2 list ['jim', 'james', 'jim', 'james', 'jim', 'james']
count of jim is = 3
sorted ascending names list using sort ['james', 'jim', 'rao', 'simi', 'stella', 'su', 'suma']
sorted descending names list using reverse ['suma', 'su', 'stella', 'simi', 'rao', 'jim', 'james']
Index of rao 4
After removing rao ['suma', 'su', 'stella', 'simi', 'jim', 'james']
After clearing the list []
'''
