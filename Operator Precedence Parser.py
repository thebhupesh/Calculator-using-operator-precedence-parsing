import numpy as np

# pop function for stack
def pop(i,j,stack):
    for k in range(i,(j-1),-1):
        stack.pop(k)
    return stack

# initializing variables and data
exp = input("Enter expression: ")
stack = []; list = []; operators = []; n = ""
data = []; data.append('$'); data.append('(')
for i in range(0,len(exp)):
    op = exp[i]
    if exp[i].isdigit():
        n += exp[i]
        op = ""
    if exp[i]=='+' or exp[i]=='-' or exp[i]=='*' or exp[i]=='/' or exp[i]=='(' or exp[i]==')' or i==(len(exp)-1):
        if len(n)!=0:
            list.append(n)
            data.append(n)
        if len(op)!=0:
            list.append(op)
            data.append(op)
            operators.append(op)
        n = ""
exp = "".join(list)

# operator precedence table
print("\nOperator Precedence Table\n")
arr = np.array(operators)
arr = np.unique(arr)
operators = arr.tolist()
for i in operators:
    print("\t",end="")
    print(i,end="")
for i in operators:
    print()
    print(i,"\t",end="")
    for j in operators:
        if i=='+':
            if j=='+':
                print(">","\t",end="")
            elif j=='-':
                print(">","\t",end="")
            elif j=='*':
                print("<","\t",end="")
            elif j=='/':
                print("<","\t",end="")
            elif j=='(':
                print("<","\t",end="")
            elif j==')':
                print(">","\t",end="")
        elif i=='-':
            if j=='+':
                print("<","\t",end="")
            elif j=='-':
                print(">","\t",end="")
            elif j=='*':
                print("<","\t",end="")
            elif j=='/':
                print("<","\t",end="")
            elif j=='(':
                print("<","\t",end="")
            elif j==')':
                print(">","\t",end="")
        elif i=='*':
            if j=='+':
                print(">","\t",end="")
            elif j=='-':
                print(">","\t",end="")
            elif j=='*':
                print(">","\t",end="")
            elif j=='/':
                print("<","\t",end="")
            elif j=='(':
                print("<","\t",end="")
            elif j==')':
                print(">","\t",end="")
        elif i=='/':
            if j=='+':
                print(">","\t",end="")
            elif j=='-':
                print(">","\t",end="")
            elif j=='*':
                print(">","\t",end="")
            elif j=='/':
                print(">","\t",end="")
            elif j=='(':
                print("<","\t",end="")
            elif j==')':
                print(">","\t",end="")
        elif i=='(':
            if j=='+':
                print("<","\t",end="")
            elif j=='-':
                print("<","\t",end="")
            elif j=='*':
                print("<","\t",end="")
            elif j=='/':
                print("<","\t",end="")
            elif j=='(':
                print("<","\t",end="")
            elif j==')':
                print("=","\t",end="")
        elif i==')':
            if j=='+':
                print(">","\t",end="")
            elif j=='-':
                print(">","\t",end="")
            elif j=='*':
                print(">","\t",end="")
            elif j=='/':
                print(">","\t",end="")
            elif j=='(':
                print("X","\t",end="")
            elif i==')':
                print(">","\t",end="")

# check validity of string
data.append(')'); data.append('$')
for i in range(0,len(data)):
    j0 = data[i]
    if j0=='+':
        j1 = data[i+1]
        stack.append(j0)
        if j1=='+':
            stack.append('>')
        elif j1=='-':
            stack.append('>')
        elif j1=='*':
            stack.append('<')
        elif j1=='/':
            stack.append('<')
        elif j1=='(':
            stack.append('<')
        elif j1==')':
            stack.append('>')
        elif j1.isdigit():
            stack.append('<')
    elif j0=='-':
        j1 = data[i+1]
        stack.append(j0)
        if j1=='+':
            stack.append('<')
        elif j1=='-':
            stack.append('>')
        elif j1=='*':
            stack.append('<')
        elif j1=='/':
            stack.append('<')
        elif j1=='(':
            stack.append('<')
        elif j1==')':
            stack.append('>')
        elif j1.isdigit():
            stack.append('<')
    elif j0=='*':
        j1 = data[i+1]
        stack.append(j0)
        if j1=='+':
            stack.append('>')
        elif j1=='-':
            stack.append('>')
        elif j1=='*':
            stack.append('>')
        elif j1=='/':
            stack.append('<')
        elif j1=='(':
            stack.append('<')
        elif j1==')':
            stack.append('>')
        elif j1.isdigit():
            stack.append('<')
    elif j0=='/':
        j1 = data[i+1]
        stack.append(j0)
        if j1=='+':
            stack.append('>')
        elif j1=='-':
            stack.append('>')
        elif j1=='*':
            stack.append('>')
        elif j1=='/':
            stack.append('>')
        elif j1=='(':
            stack.append('<')
        elif j1==')':
            stack.append('>')
        elif j1.isdigit():
            stack.append('<')
    elif j0=='(':
        j1 = data[i+1]
        stack.append(j0)
        if j1=='+':
            stack.append('<')
        elif j1=='-':
            stack.append('<')
        elif j1=='*':
            stack.append('<')
        elif j1=='/':
            stack.append('<')
        elif j1=='(':
            stack.append('<')
        elif j1==')':
            stack.append('X')
        elif j1.isdigit():
            stack.append('<')
        elif j1=='$':
            stack.append('X')
    elif j0==')':
        j1 = data[i+1]
        stack.append(j0)
        if j1=='+':
            stack.append('>')
        elif j1=='-':
            stack.append('>') 
        elif j1=='*':
            stack.append('>')
        elif j1=='/':
            stack.append('>')
        elif j1=='(':
            stack.append('X')
        elif j1==')':
            stack.append('>')
        elif j1.isdigit():
            stack.append('X')
    elif j0.isdigit():
        j1 = data[i+1]
        stack.append('id')
        if j1=='(':
            stack.append('X')
        else:
            stack.append('>')
    elif j0=='$':
        if i==0:
            stack.append(j0)
            stack.append('<')
        elif i==(len(data)-1):
            stack.append('>')
            stack.append(j0)
flag = 1
while i<len(stack):
    if stack[i]=='>':
        j = i
        while j!=0:
            if stack[j]=='<':
                break
            else:
                j -= 1
        if j>=0:
            stack = pop(i,j,stack)
            i = 0
        else:
            i += 1
    elif stack[i]=='X':
        break
    else:
        i += 1
if "".join(stack)!='$$':
    flag = 0

# output for the expression
print("\n")
if flag==1:
    print("Valid Input")
    print("Answer:",round(eval(exp),5))
elif flag==0:
    print("Invalid Input")