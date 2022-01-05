from zipfile import ZipFile
from os import path, walk

root = path.join('..', 'test')

def zipFiles(root):
    zipName = ''.join(path.basename(root) + '.zip')
    backupZipFile = ZipFile(zipName , 'w')
    print(f'Creating {zipName}')
    for directory, subDirList, fileList in walk(root):
        print(f'Adding files in {directory}')
        backupZipFile.write(directory)
        for name in fileList:
            backupZipFile.write(path.join(directory, name))   
    backupZipFile.close()
    print('Done!')
zipFiles(root)