#!/usr/bin/env python3

# even odd checker function
def is_even(num):
    return num % 2 == 0

# is any number is even
def is_any_even(nums):
    for num in nums:
        if is_even(num):
            return True
    return False