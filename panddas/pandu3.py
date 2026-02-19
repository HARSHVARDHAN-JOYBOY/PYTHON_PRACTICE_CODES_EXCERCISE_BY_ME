import pandas as pd
data={'day1':1000,'day2':10000,'day3':100000}

a=pd.Series(data,index=['day1','day3'])

print(a)
    