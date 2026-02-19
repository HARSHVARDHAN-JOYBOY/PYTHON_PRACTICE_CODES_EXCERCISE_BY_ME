import os

file= open("tempesh.txt",'w')
lines=['Ram ','Rama ','Raghava ','Raghupati ','Purushottam ']
file.writelines(lines)
file.close()