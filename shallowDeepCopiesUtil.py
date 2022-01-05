# a = [[1, 2, 3], [4, 3, 5]]
# b = list(a) # makes a shallow copy

# print('Before')
# print(a)
# print(b)

# a[0][0] = 'x'

# print('After')
# print(a)
# print(b)

##########################
#### DEEP COPY
#########################

import copy
a = [[1, 2, 3], [4, 3, 5]]
b = copy.deepcopy(a)

print('Before')
print(a)
print(b)

a[0][0] = 'x'

print('After')
print(a)
print(b)
