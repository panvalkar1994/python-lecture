# simple dict with key value
# my_dict = {'key1':'value1', 'key2':'value2'}
# print(my_dict)

prices_lookup = {
    'apple':100,
    'orange':50
}

print(prices_lookup['apple'])

# nested dict
nested_dict = {
    'main':'This is Header',
    'sub':{
        'main':'This is sub header'
    }
}

print(nested_dict['sub']['main'])

# add new key value
add_dict = {
    'k1':100
}

add_dict['k2'] = 200

# print(add_dict)

# print all values 
print(add_dict.values())

# print all keys
print(add_dict.keys())

# print pairs
print(nested_dict.items())