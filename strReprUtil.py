class Glass:
    
    def __init__(self, reflct):
        self.reflct = reflct
    
    def __str__(self):
        print('inside __str__ method')
    
    def __repr__(self):
        print('inside __repr__ method')

glass = Glass('MIRROR')

# This will all statements will use class __str__ method
'{}'.format(glass)
str(glass)
print(glass)

#OUTPUT
# inside __str__ method

# This will use __repr__ method 
# glass

#OUTPUT
# inside __repr__ method