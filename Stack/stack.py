stack=[]

stack.append(1)
stack.append(2)
stack.append(3)
print(stack)

while stack:
    print(stack.pop())

def parathesis(s):
    stack = []
    completed = {")": "(", "]": "[", "}": "{"}
    for p in s:
        if p in completed:
            if stack and completed[p]==stack[-1]:
                stack.pop()
            else:
                return False
        else:
            stack.append(p);
    return True if not stack else False


print(parathesis('[]'))