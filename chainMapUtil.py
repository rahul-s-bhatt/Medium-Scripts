from collections import ChainMap
d1 = { 'a': 1, 'b': 2 }
d2 = { 'c': 3, 'd': 4 }
chain = ChainMap(d1, d2)

# ChainMap searches each collection in the chain
# from left to right until it finds the key (or fails):
print(chain)

# OUTPUT 
# ChainMap({'a': 1, 'b': 2}, {'c': 3, 'd': 4})