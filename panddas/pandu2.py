import pandas as pd
data={
    "Student name":["Shubham","Harshvardhan","Shriram","Jivesh","Chetan","Abhishekh","Sushant","Roshan"],"Favorite Subject":["Agriculture","Pyhton","UIUX","Python","React-js","Java","CPP","English"]
}

newdata=pd.DataFrame(data,index=['A','B','C','D','E','F','G','H'])
print(newdata)
print(newdata.loc[['H','B']])
