l=[12,5,45,45,34,2,43,33]
ll=[[1,"Ram",22],[2,"Bharat",21.9],[3,"Lakshman",21.8],[4,"Shatrughn",21.7]]
d={"lambo":30,"ferrari":40,"M5":90}
t=("sam","yajur","riga","atharv")
s="vande mataram"
st={46,65,8,89,34}
print(sorted(l,reverse=True))
print("\n")
print(sorted(ll,key= lambda item:item[2],reverse=True))
print("\n")

print(sorted(d))
print(sorted(d.items()))
print(sorted(d.values()))
print(sorted(d,key = lambda item:item[1]))

print(sorted(t))

print(sorted(s))

print(sorted(st))










