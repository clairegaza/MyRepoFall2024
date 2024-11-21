my_list = [11, 22, 33, 44, 22, 55, 66, 22, 22, 77, 88, 99]
my_set = set(my_list)
# create an empty set
print(my_set)

import math
result = abs(9) + math.sqrt(3)
print(int(result))

# abs(x)      Returns the absolute value of x.
# min(x, y)   Returns the smaller of x and y.
# max(x, y)   Returns the larger of x and y.
# round(x)        Returns x to the nearest integer or
# round(x, digits)to the specified number of digits.

# The += operator works for string concatenation, too:
word = 'fire'
word += 'truck'
print(word)

#Use the str function to covert numbers to strings before concatenation:
subtotal = 14.75
subtotal_statement = 'The subtotal is ' + str(subtotal)
print(subtotal_statement)

# The range function takes an integer argument n and produces a
# sequence of values from 0 to n-1.
for num in range(5):
    print(num)

for i in range(50, 60):
    print(i, end=' ')

print()

# SCANNER / INPUT STATEMENTS
num = float(input('Enter a number greater than 100: '))
while num <= 100:
    num = float(input('Invalid. Please reenter: '))
print('Moving on...')

capitals = {'Maryland' : 'Annapolis',
 'New York' : 'Albany',
 'California' : 'Sacramento',
 'Delaware' : 'Dover'}
print('The capital of New York is', capitals.get('New York'))

# To remove the value of a dictionary entry, use its key.
capitals.pop('Maryland')

#Iterate the keys in a dictionary using a for loop.
for key in capitals:
    print(key)
#Iterate the values in a dictionary with the values method.
for value in capitals.values():
    print(value)

#DICTIONARY EXAMPLE
nums = [27, 31, 77, 49, 69, 31, 69, 31, 70, 36, 12, 88, 31, 69, 31, 55,
31, 31, 69, 27, 89, 31, 55, 55, 69, 55, 49, 88, 49, 55, 49, 12, 31, 69,
55, 98, 31, 39, 88, 36, 69, 69, 77, 88, 69, 89, 12, 27, 31, 27]
counts = {}
for num in nums:
    if num not in counts:
        counts[num] = 1
    else:
        counts[num] += 1
for num in sorted(counts, key=counts.get, reverse=True):
    print(num, 'appears', counts[num],'time' if counts[num] == 1 else 'times')  

names = ['Tim', 'Mary', 'Jane', 'Joe', 'Steve', 'Eve']
print(names)
# reverse will reverse the order of the list
names.reverse()
print(names)
# sort puts items in their natural order
names.sort()
print(names)