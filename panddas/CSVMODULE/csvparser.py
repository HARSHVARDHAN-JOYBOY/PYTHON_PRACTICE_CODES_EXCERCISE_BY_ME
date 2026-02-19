import csv
from statistics import mean

with open('D:\pythonprojectsand all\OSMOD\panddas\CSVMODULE\datacsv1.csv','r')as file:
    reader=list(csv.DictReader(file))

    ages=[]
    salaries=[]


    
    for i in reader:
        print(f"\n Name : {i['Name']} \n Age : {i['Age']} \n Salary : {i['Salary']} \n")

    for col in reader:
        ages.append(int(col['Age']))
        salaries.append(float(col['Salary']))
    print("-----Salary Stats-----")
    print("----------------------")
    print(f"Total rows : {len(ages)} \n")
    print(f"Average Age : {mean(ages):.2f} \n")
    print(f"Minimum Ages : {min(ages)} \n")
    print(f"Maximum : {max(ages)} \n")
    print(f"Average Salary : {mean(salaries):.2f} \n")
    print(f"Minimum Salary : {min(salaries)} \n")
    print(f"Maximum Salary : {max(salaries)} \n")



