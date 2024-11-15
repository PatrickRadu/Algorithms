def brute(nums):
    numSet=set(nums)
    numSet=list(numSet)
    if len(numSet)==0: return 0
    Max=1
    k=1
    print(numSet)
    for i in range(1,len(numSet)):
        # print(numSet[i],numSet[i-1])
        print(k,Max)
        if numSet[i]==numSet[i-1]+1:
            k+=1
            Max = max(Max, k)
        else:
            Max = max(Max, k)
            k=1
    return Max




print(brute([0,3,2,5,4,6,1,1]))