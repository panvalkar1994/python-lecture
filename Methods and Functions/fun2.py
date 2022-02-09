#!/usr/bin/env python3

# Warm up problem set

# LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers are even, but returns the greater if one or both numbers are odd
def lesser_of_two(num1: int, num2: int) -> int:
    if num1 % 2 == 0 and num2 % 2 == 0:
        return min(num1, num2)
    return max(num1, num2)

# print(lesser_of_two(2,4))
# print(lesser_of_two(2,5))

# ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter
def animal_crackers(two_words:str)->bool:
    word_list = two_words.split()
    return word_list[0][0] == word_list[1][0]

# print(animal_crackers('Levelheaded Llama'))
# print(animal_crackers('Crazy Kangaroo'))

# MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False
def makes_twenty(num1:int, num2:int)->bool:
    twenty = 20
    if twenty in (num1, num2):
        return True
    if num1 + num2 == twenty:
        return True
    return False

# print(makes_twenty(20,10))
# print(makes_twenty(2,3))