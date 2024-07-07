"""
Dictionary - Dictionaries are used to store data values in key:value pairs.

Operations and Time complexity-

O(1) --> k in d, Get Item, Set Item[1], Delete Item
O(n) --> Copy[3], Iteration[3]



"""

sample_dict = {'a': 1, 'b': 2, 'c': 3}

sample_dict.keys()  # returns list of keys of dictionary
sample_dict.values()  # returns list of values of dictionary
sample_dict.get('a')  # returns value for any corresponding key
sample_dict.items()  # returns [('a',1),('b',2),('c',3)]
# NOTE : items() Returns view object that will be updated with any future changes to dict

sample_dict.copy()  # returns copy of the dictionary

sample_dict.pop('a')  # pops key-value pair with that key
sample_dict.popitem()  # removes most recent pair added
sample_dict.setdefault('KEY', "DEFAULT_VALUE")  # returns value of key, if key exists, else default value returned
# If the key exist, this parameter(DEFAULT_VALUE) has no effect.
# If the key does not exist, DEFAULT_VALUE becomes the key's value. 2nd argument's default is None.
sample_dict.update({'KEY': 'VALUE'})  # inserts pair in dictionary if not present,
# if present, corresponding value is overriden (not key)
# Default dict ensures that if any element is accessed that is not present in the dictionary it will be created
# and error will not be thrown (which happens in normal dictionary).
