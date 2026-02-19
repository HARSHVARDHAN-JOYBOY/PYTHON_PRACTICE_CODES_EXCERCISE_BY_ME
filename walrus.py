def slowfunc():
    print("somthing..........")
    print("somthing..........")
    print("somthing..........")
    print("somthing..........")
    print("somthing..........")
    return 70
# a=slowfunc()
if((a:=slowfunc())>10):
    print(f"ohhhhhh !!! ",a)
else:
    print("no gr3ter !")
