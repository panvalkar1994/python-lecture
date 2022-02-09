#!/usr/bin/env python3

# *args in function
def average(*args):
    return sum(args)/len(args)

num_avg = average(1,2,3,4,5)
print('average: {}'.format(num_avg))

# **kwargs in function

def my_fav(**kwargs):
    print(kwargs)
    if 'fruit' in kwargs:
        print('My favourite fruit is {}'.format(kwargs['fruit']))
    if 'car' in kwargs:
        print('My Favourite Car is {}'.format(kwargs['car']))

my_fav(fruit='Mango', car='Tesla')