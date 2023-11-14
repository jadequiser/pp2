import os

def lol(path):
    if os.path.exists(path):
        print("The path exists")
        f=os.path.basename(path)
        d=os.path.dirname(path)
        print(f"Filename: {f}")
        print(f"Directory: {d}")
    else:
        print(f"The path doesnt exist.")
        return
x = input()
lol(x)
