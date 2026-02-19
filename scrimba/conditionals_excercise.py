def cdays(month):
    thirtyone=["january","march","may","july","august","october","december"]
    thirty=["february","april","june","september","november"]
    
    if month in thirty:
        print("30")
    elif month in thirtyone:
        print("31")
    elif month=="february":
        print("28/29")
    else :
        print("Wrong choice ")
        
cdays(input("Enter month name :").lower())




# or


def daysinmonth(month):
    days={
        "january":31,
        "february":"28 or 29",
        "march":31,
        "april":30,
        "may":31,
        "june":30,
        "july":31,
        "august":31,
        "september":30,
        "october":31,
        "november":30,
        "december":31
    }

    print(days.get(month,"Invalid choice !"))
    
    
daysinmonth(input("Enter month : ").lower())

