arr=[i for i in range(5)]

def bf(s):
    Max=0;
    char_set=set()
    l=0
    res=0
    for r in range(len(s)):
        while s[r] in char_set:
            char_set.remove(s[l])
            l+=1
        char_set.add(s[r])
        res=max(res,r-l+1)
    return res

print(bf("aab"))



def slidingWindow(s):
    res=0
    charSet=set()
    l=0
    for r in range(len(s)):
        while s[r] in charSet:
            charSet.remove(s[l])
            l+=1
        charSet.add(s[r])
        res=max(res,r-l+1)
    return res

print(slidingWindow("zxyzxyz"))





def problemDoneAgain(str):
    l=0
    res=0
    charSet=set()
    for r in range(len(str)):
        while str[r] in charSet:
            charSet.remove(str[l])
            l+=1
        charSet.add(str[r])
        res=max(res,r-l+1)
    return res

print(problemDoneAgain("zxyzxyz"))












