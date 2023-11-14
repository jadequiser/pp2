import os
path_of_file = input()

try:
    os.remove(path_of_file)
    print(f"'{path_of_file}' deleted.")
except OSError as e:
    print(f"Error: {e}")





