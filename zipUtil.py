listOfUsers = ['a', 'b', 'c', 'd']
listOfResponse = ['I m a', 'I m b', 'I m c']

for user, response in zip(listOfUsers, listOfResponse):
    print(user, ': ', response)