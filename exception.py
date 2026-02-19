while True:
    try:
        a=int(input("Enter number 1 :"))
        b=int(input("Enter number 2 :"))

        print(f"The Division of these two is : {a/b}")
    
    except ValueError:
        print("Hey please don do bad typecasting !")

    except ZeroDivisionError:
        print("Hey please dont divide with zero !")    
        
    except Exception as e:
        print("Error ocured in this one : ",e)

    except :
        if a==0 or b==0:
            raise ValueError("Please dont use 0 in division !!! ")
    #    this is use to show exception handling

# a=int(input("Enter number 1 :"))
# b=int(input("Enter number 2 :"))
# print(f"The Division of these two is : {a/b}")
# if a==0 or b==0:
#     raise ValueError("Please do not divide with zero !")

