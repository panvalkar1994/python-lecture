#!/usr/bin/env python3

# print characters from string
for char in "Hello World":
    print(char)

# ignoring variable
for _ in "Hello":
    print("cool!")


# tuple unpacking
my_tup_list = [(1,2), (3,4), (5,6)]
for a, b in my_tup_list:
    print(a, b)

d = {
    'k1':'v1',
    'k2':'v2',
    'k3':'v3'
}

# by default dict iter gives keys
for item in d:
    print(item)

# dict unpacking
for k,v in d:
    print(f"{k} : {v}")

# getting only values out of dict
# for _, v in d:
#     print(v)
for value in d.values():
    print(value)