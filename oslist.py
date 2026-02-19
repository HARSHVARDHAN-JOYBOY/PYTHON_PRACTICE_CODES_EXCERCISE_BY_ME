import os

folder= os.listdir("python")
for f in folder:
    print(folder)
    print(os.listdir(f"python/{f}"))
