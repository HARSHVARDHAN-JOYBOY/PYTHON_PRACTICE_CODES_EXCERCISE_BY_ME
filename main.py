import os

if(not os.path.exists("python")):
    os.mkdir("python")

for i in range(0, 100):
    #os.mkdir(f"python/Tutorial{i+1}")
    os.rename(f"python/TutorialDay{i+1}",f"python/TutorialDay {i+1}")

