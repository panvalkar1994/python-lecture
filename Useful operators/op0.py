#!/usr/bin/env python3

# print numbers upto 10
for num in range(10):
    print(num)

# enumerate
word = "Hello World"
for index, letter in enumerate(word):
    print(index, letter)

# zip
l1 = [1, 2, 3, 4]
l2 = ['One', 'Two', 'Three', 'Four']
for item in zip(l2, l1):
    print(item)

# in : for checking if in the collection
print( 5 in l1)
print( 'H' in word)

# min, max
print(min(l1), max(l1))