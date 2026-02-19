try:
    a= int(input("Enter first number: "))
    b= int(input("Enter second number: "))

    print("what kind of operation do you want to perform \n Addition : + \n Substraction : - \n Multiplication : * \n Division : / \n Modulus : % \n Exit : x \n")

    o=input("Enter your choice : ")
    match o:
        case "+":
            print(f"result : {a+b}")
        case "-":
            print(f"result : {a-b}")
        case "*":
            print(f"result : {a*b}")
        case "/":
            print(f"result : {a/b}")
        case "%":
            print(f"result : {a%b}")
        case default:
            print(f"result exit")


except Exception as e:
    print(" An error occured ! pleasen enter a valid input ! ")