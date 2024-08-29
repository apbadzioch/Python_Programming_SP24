# List methods: append, insert, extend, sort, reverse, clear, pop, index, count

# empty list
names = []

# append
names.append('andy')
names.append('badzioch')
print('appended with', names)

# insert
names.insert(0, 'mister')
print('inserted mister at the beginning', names)
names.insert(len(names), 'rocks')
print('inserted rocks at the end', names)

# add a name to the end of the list
names.append('patrick')
print('used append to add at the end', names)

# extend
names1 = ('mike', 'tony')
names.extend(names1)
print('extended with new names', names)

# count
names2 = names1 * 3
print('names2 list', names2)
print('count of tony is:', names2.count("tony"))

# sort
names.sort()
print('sorted list:', names)

# reverse
names.reverse()
print('reversed list:', names)

# index
i = names.index('andy')
print('index of andy by using i to hold marker:', i)
print('index of andy:', names.index('andy'))

# pop
names.pop(i)
print('removing andy:', names)

# clear
names.clear()
print('after clearing the list:', names)


