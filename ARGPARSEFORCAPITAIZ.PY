import argparse

parse= argparse.ArgumentParser(description="for capitalizing word or decapitalizing ")
parse.add_argument("word",type=str,help="A string")
parse.add_argument("operation",choices=["cap","sml","ctl","titl"],help="operation to perform")

args=parse.parse_args()
print(args)

if(args.operation=="cap"):
    print(args.word.upper())
if(args.operation=="sml"):
    print(args.word.lower())
if(args.operation=="ctl"):
    print(args.word.capitalize())
if(args.operation=="titl"):
    print(args.word.title())



