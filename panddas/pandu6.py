import pandas as pd
data={
"Name":{0:"Harsh",1:"Pavan",2:"Aadi",3:"Shubh",4:"ShriRam",5:"Jivesh"},"Rn":{0:1,1:2,2:3,3:4,4:5,5:6},"Age":{0:21,1:20,2:22,3:15,4:25,5:34}
}
# df=pd.DataFrame(data,index=["I","II","III","IV","V","VI"])
df=pd.DataFrame(data)

print(df)

