import os

def dir(path):
    vse = os.listdir(path)
    directories = [item for item in vse if os.path.isdir(os.path.join(path, item))]
    print("directories:", directories)

def files(path):
    vse = os.listdir(path)
    files = [item for item in vse if os.path.isfile(os.path.join(path, item))]
    print("files:", files)

def all(path):
    vse = os.listdir(path)
    print("all directories and files:", vse)

specified_path = input()

dir(specified_path)
files(specified_path)
all(specified_path)



