# append to file
with open('test.txt', mode='a') as f:
    f.write('\nline 5')


data = ""
# using with open so no need to close explicitly 
with open('test.txt', mode='r') as f:
    data = f.read()

print(data)