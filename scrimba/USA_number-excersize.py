while True:
    num=input(f"Enter a number : ")
    num3=str()
    num1=num.strip()
    for c in "-().":
        num1=num1.replace(c, " ")

    numt="".join(num1.split(" "))
    if len(numt) ==10:
        fnum=f"({numt[0:3]}) {numt[3:6]}-{numt[6:10]}"
        print(f"{fnum}")
    else:
        print("nope")
    break

    