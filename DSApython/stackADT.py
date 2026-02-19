MAX=10
stack=[0]*MAX
top=-1
# alpha=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
# numer=[0,1,2,3,4,5,6,7,8,9]





def push(x):
    global top
    if top>=MAX-1:
        print("stack overflow !")
        return
    top+=1
    stack[top]=x

def pop():
    global top
    if top==-1:
        print("Stack underflow !")
        return
    val=stack[top]
    top-=1
    return val

def precidence(x):
    if x=="^":
        return 3
    if x=="/" or x=="*":
        return 2
    if x=="+" or x=="-":
        return 1
    return 0

def main():
    i,j=0,0
    global top
    infix=input("enter infix expression :")
    postfix=[]

    for ch in infix:
        ch=infix[i]
        if ch.isalnum():
            postfix.append(ch)
            j+=1
        elif(ch=='('):
            push(ch)
        elif(ch==")"):
            while(stack[top]!="("):
                postfix.append(stack[top])
                j+=1
                top-=1
            pop()
        else:
            while(top!=-1 and precidence(stack[top])>=precidence(ch)):
                postfix.append(pop())
                j+=1
            push(ch)
        i+=1
    while(top!=-1):
        postfix.append(pop())
        j+=1
    print(f"Postfix is  : {''.join(postfix)} !")

if __name__=="__main__":
    main()





















