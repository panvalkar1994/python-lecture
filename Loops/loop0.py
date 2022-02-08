#!/usr/bin/env python3

# iterable: It means we can iterate through this object
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for num in my_list:
#     print(num, end=" ")


# print all even numbers
for num in my_list:
    if num % 2 == 0:
        print(num)


list_sum = 0
for num in my_list:
    list_sum = list_sum + num

print(f"My list sum: {list_sum}")