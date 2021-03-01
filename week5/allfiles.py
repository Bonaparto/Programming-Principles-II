import os

def dirs(path):
    for i in os.listdir(path):
        i_path1 = os.path.join(path, i)
        if os.path.isfile(i_path1):
            print(f'FILE: {i_path1}')
        else:
            dirs(i_path1)

ULR = os.getcwd()
for i in os.listdir():
    i_path = os.path.join(ULR, i)
    if os.path.isfile(i_path):
        print(f'FILE: {i_path}')
    else:
        dirs(i_path)