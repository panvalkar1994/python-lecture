my_list = [1, 2, 3] # list of ints
mixed_list = [1, 'two', False, my_list] # mixed list

# length of list
print(len(mixed_list)) # 4

# concat
print(my_list + my_list)

# mutable
mixed_list[0] = 'One'
# print(mixed_list)

# append
my_list.append(4)
print(my_list)

# remove item from end
popped_item = my_list.pop()
print(popped_item)

# remove item using index
print(my_list.pop(0)) # remove first elem


unsorted_list = [4,3,1,2]
# sort list in place
# unsorted_list.sort() 

# return sorted list
sorted_list = sorted(unsorted_list)
print(sorted_list)
