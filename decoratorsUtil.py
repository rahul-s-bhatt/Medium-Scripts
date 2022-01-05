def uppercase(func):
    def wrapper():
        originalResult = func()
        modifiedResult = originalResult.upper()
        return modifiedResult
    return wrapper

@uppercase
def greet():
    return 'Hello World!'

print(greet())

# OUTPUT 
# HELLO WORLD!