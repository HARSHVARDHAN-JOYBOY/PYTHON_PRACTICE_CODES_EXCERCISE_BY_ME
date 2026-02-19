import argparse

parser=argparse.ArgumentParser(description="Simple Calculator")
parser.add_argument("num1",type=float,help="First Number")
parser.add_argument("num2",type=float,help="Second Number")
parser.add_argument("operation",choices=["add","sub","mul","div","mod","sq","cb"], help="operation to perform")

args=parser.parse_args()
print(args)

if(args.operation == "add"):
    print(f"the result is {args.num1 + args.num2}")
elif(args.operation == "sub"):
    print(f"the result is {args.num1 - args.num2}")
elif(args.operation == "mul"):
    print(f"the result is {args.num1 * args.num2}")
elif(args.operation == "div"):
    print(f"the result is {args.num1 / args.num2}")        
elif(args.operation == "mod"):
    print(f"the result is {args.num1 % args.num2}")
elif(args.operation == "sq"):
    print(f"the result is {args.num1 * args.num1}")
elif(args.operation == "cb"):
    print(f"the result is {args.num1 * args.num1 * args.num1}")  
else:
    print("Some error occured :")

