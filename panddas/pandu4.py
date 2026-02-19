import pandas as pd

data={
    "Game":["BGMI","GTA-V","PALWORLD","FREE_FIRE","FORZA-HORIZON"],"Size":[10,100,30,3,110]
}

df=pd.DataFrame(data,index=["Top-1","Top-2","Top-3","Top-4","Top-5"])
print(df.loc[["Top-1","Top-3"]])

