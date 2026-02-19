def divby5(x):
    if x>5:
        return True 
    else:
        return False
    
a=[12,534,325,5,4544,42,55,27,254,186,4757,756,88,55,54,88,34,374,777,648,256,73,6,6,3,3]
print(a)

new =list(filter(divby5,a))

print(new)