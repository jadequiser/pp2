import string
import os

name = "bukviki"

if not os.path.exists(name):
    os.makedirs(name)

for letter in string.ascii_uppercase:
    filepath=os.path.join(name, letter + ".txt")
    with open(filepath, "w") as f:
        f.write(letter)
