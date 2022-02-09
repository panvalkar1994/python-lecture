#!/usr/bin/env python3

# Level 1 Problems

# OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
def old_macdonald(word:str)->str:
    char_list = list(word)
    char_list[0] = char_list[0].upper()
    if len(char_list)>=4:
        char_list[3] =  char_list[3].upper()
    return "".join(char_list)

# print(old_macdonald('macdonald'))
# print(old_macdonald('mac'))

# MASTER YODA: Given a sentence, return a sentence with the words reversed
def master_yoda(sentence:str)->str:
    return " ".join(reversed(sentence.split()))

# print(master_yoda('I am home'))
# print(master_yoda('We are ready'))

# ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200
def almost_there(n:int)->bool:
    if 10>=abs(100-n) or 10>=abs(200-n):
        return True
    return False

# print(almost_there(101))
# print(almost_there(99))
# print(almost_there(121))
# print(almost_there(210))