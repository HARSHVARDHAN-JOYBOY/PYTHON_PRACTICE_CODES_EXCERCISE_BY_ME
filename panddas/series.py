import pandas as pd
a=[2,7,1]
# myser=pd.Series(a)
# print(myser)
# print(myser[1])

# myser=pd.Series(a,index=['first','second','third'])
myser=pd.Series(a,index=['first','second','third'])
print(myser['second'])