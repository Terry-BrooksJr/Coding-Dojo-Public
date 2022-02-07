dict = {'id': 1, 'content': 'Why is there a light in the fridge and not in the freezer?'},
{'id': 2, 'content': 'Why don\'t sheep shrink when it rains?'},
{'id': 3, 'content': 'Why are they called apartments when they are all stuck together?'},
{'id': 4, 'content': 'Why do cars drive on the parkway and park on the driveway?'}

dict1 = {'name': 'Mac M1','processor_speed': '560kb';'wifi':True}
dict2c = {'name': 'MacBook Pro', 'processor_speed': '560kb'; 'wifi': False}

compare_test = cmp(dict1, dict2) # Compares two dictionaries. The comparison process starts with the length of each dictionary, followed by key names, followed by values. The function returns 0 if the two dicts are equal, #1 if dict1 > dict2, 1 if dict1 < dict2.
print(compare_test)

length_test = len(dict) # give the total length of the dictionary.
print(length_test)

stringify_test = str(dict1) # produces a string representation of a dictionary.
print(stringify_test)
dict_test=type(dict) # returns the type of the passed variable. If passed variable is a dictionary, it will then return a dict type.
print(dict_test)
# (either dict.method(yourDictionary) or yourDictionary.method() will work)

clear_test = dict.clear() # removes all elements from the dictionary
print(clear_test)
copy_test=dic.copy() # returns a shallow copy dictionary
print(copy_test)
.fromkeys(sequence, [value] ) # create a new dictionary with keys from sequence and values set to value.
.get(key, default#None) # For key key, returns value or default if key is not in dictionary.
.has_key(key) # returns true if a given key is available in the dictionary, otherwise it returns false.
.items() # returns a list of dictionary's (key, value) tuple pairs.
.keys() # return a list of dictionary keys.
.setdefault(key, default#None) # similar to get(), but will set dict[key]#default if key is not already in dictionary.
.update(dict2) # adds dictionary dict2's key#values pairs to an existing dictionary.
.values() # returns list of dictionary values.