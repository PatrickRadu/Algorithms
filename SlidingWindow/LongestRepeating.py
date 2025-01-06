def longestRepeatingbf(array,k):
    maxLen=0
    diffChar=dict()
    l=0
    for r in range(len(array)):
        if array[r] not in diffChar.keys():
            diffChar[array[r]]=1
        else:
            diffChar[array[r]]+=1
    for value in diffChar.values():
        MaxLen=max(maxLen,value)
    return value+k
    print(diffChar)


def slidingWindow(s,k):
    res=0
    charSet=set(s)
    for c in charSet:
        count=l=0
        for r in range(len(s)):
            if s[r]==c:
                count+=1
            while(r-l+1)-count>k:
                if s[l]==c:
                    count-=1
                l+=1
            res=max(res,r-l+1)
    return s
print(longestRepeatingbf('AAABABB',2))
