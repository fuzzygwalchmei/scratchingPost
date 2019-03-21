import os
import time

#path=input("Whats the folder?: ")
curTime = time.strftime('%B %A %d %Y')
print(curTime)


# for i in os.scandir(path):
#     if i.is_file():
#         print('File: ' + i.path)
#     elif i.is_dir():
#         print('Folder: '+ i.path)