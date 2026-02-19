#write a code for a simple csv reading and json reading using pandas
import pandas as pd
data={'day1':1000,'day2':10000,'day3':100000}
a=pd.Series(data,index=['day1','day3'])
print(a)
# df=pd.read_csv("D:\pythonprojectsand all\OSMOD\panddas\data23.csv")
df=pd.read_json("D:\pythonprojectsand all\OSMOD\panddas\data24.json")
print(df)           
# print(df.head()) 
# print(pd.options.display.max_rows)
# print(newdata)
# print(newdata.loc[['H','B']])
# print(newdata)

