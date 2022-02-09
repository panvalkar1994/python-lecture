#!/usr/bin/env python3

# Level 2 Problems

# FIND 33:
# Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.


from typing import List


def has_33(nums:List[int])->bool:
    for i in range(0, len(nums)-1):
        if nums[i] == 3 and nums[i+1] == 3:
            return True
    return False

# print(has_33([1, 3, 3]))
# print(has_33([1, 3, 1, 3]))
# print(has_33([3, 1, 3]))

# PAPER DOLL: Given a string, return a string where for every character in the original there are three characters
def paper_doll(inp_str:str)->str:
    out_str = ""
    for char in inp_str:
        out_str += char*3
    return out_str

# print(paper_doll('Hello'))
# print(paper_doll('Mississippi'))

# BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'
def blackjack(a, b, c):
    total = a + b + c
    if total <= 21:
        return total
    if 11 in [a,b,c] and total <= 31:
        return total - 10
    return 'BUST'

# print(blackjack(5,6,7))
# print(blackjack(9,9,9))
# print(blackjack(9,9,11))

# SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers.
def summer_69(arr):
    total = 0
    is_allowed = True
    for num in arr:
        if num == 6 and is_allowed == True:
            is_allowed = False
        elif is_allowed == False and num == 9:
            is_allowed = True
        elif is_allowed == True:
            total += num
    return total


print(summer_69([1, 3, 5]))
print(summer_69([4, 5, 6, 7, 8, 9]))
print(summer_69([2, 1, 6, 9, 11]))

