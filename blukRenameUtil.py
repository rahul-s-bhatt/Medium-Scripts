import os

root = os.path.join('..', 'test')

targetName = "textFile"
iter = 1

for directory, subDirList, fileList in os.walk(root):
    for name in fileList:
        sourceName = os.path.join(directory, name)
        modifiedName = os.path.join(directory, f'{targetName} {iter}')
        iter  += 1
        print(f'Changed file name from: {sourceName} to {modifiedName}')
        os.rename(sourceName, modifiedName) 