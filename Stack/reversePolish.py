


def reversePolish(tokens):
    stack=[]
    for c in tokens:
        if c=='+':
            a,b=stack.pop(),stack.pop()
            stack.append(a+b)
        elif c=='-':
            a, b = stack.pop(), stack.pop()
            stack.append(b-a)
        elif c=='*':
            a, b = stack.pop(), stack.pop()
            stack.append(a*b)
        elif c=='/':
            a,b=stack.pop(), stack.pop()
            stack.append(int(float(b)/a))
        else:
            stack.append(int(c))
    return stack[0]

print(reversePolish(["1","2","+","3","*","4","-"]))
