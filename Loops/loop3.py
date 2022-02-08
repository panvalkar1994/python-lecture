#!/usr/bin/env python3

# continue :to go back to top of closest loop
for char in "Hello World":
    if char == 'o':
        continue
    print(char, end='')


# break :to break out of loop
x = 0
while True:
    if x > 10:
        print('breaking out of the loop')
        break
    print(x)
    x += 1
