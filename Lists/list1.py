#!/usr/bin/env python3


# normal way
word = 'Hello'
char_list = []

for char in word:
    char_list.append(char)


# List comprehension
new_list = [char for char in word]

# if statement in
even = [num for num in range(1,11) if num % 2 == 0]
print(even)
