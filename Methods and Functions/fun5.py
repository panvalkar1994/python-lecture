#!/usr/bin/env python3

# CHALLENGING PROBLEMS
# SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order
def spy_game(nums):
    code = [0, 0, 7]
    for num in nums:
        if len(code) == 0:
            return True
        elif num == code[0]:
            code.pop(0)
    return len(code) == 0

# print(spy_game([1,2,4,0,0,7,5]))
# print(spy_game([1,0,2,4,0,5,7]))
# print(spy_game([1,7,2,0,4,5,0]))

# COUNT PRIMES: Write a function that returns the number of prime numbers that exist up to and including a given number
def is_prime(num, primes):
    for p in primes:
        if num % p == 0:
            return False
    return True

def count_primes(num):
    if num < 2: 
        return 0
    primes = [2]
    for num in range(3, num+1):
        if is_prime(num, primes):
            primes.append(num)
    return len(primes)
    
# print(count_primes(100))