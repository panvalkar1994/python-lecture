# string immutablity
name = "Sam"
# name[0] = 'P' # this will throw an err as strings are immutable
name = "P" + name[1:]  # this works as redefined value for name
# print(name)

# repeat strings
snore = 'z' * 10
print(snore)


# methods on strings

hello = 'Hello World'

# upper case
# print(hello.upper())

# lower case
print(hello.lower())

# split string => using white space
print(hello.split())
