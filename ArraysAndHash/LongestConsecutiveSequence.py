def brute(nums):
    numSet = set(nums)
    numSet = list(numSet)
    if len(numSet) == 0: return 0
    Max = 1
    k = 1
    print(numSet)
    for i in range(1, len(numSet)):
        # print(numSet[i],numSet[i-1])
        print(k, Max)
        if numSet[i] == numSet[i - 1] + 1:
            k += 1
            Max = max(Max, k)
        else:
            Max = max(Max, k)
            k = 1
    return Max


# print(brute([0,3,2,5,4,6,1,1]))


def SortedSol(nums):
    if not nums:
        return 0
    res=0
    nums.sort()
    curr,streak=nums[0],0
    i=0
    while i<len(nums):
        if curr!=nums[i]:
            curr=nums[i]
            streak=0
        while i<len(nums) and nums[i]==curr:
            i+=1
        streak=streak+1
        curr=curr+1
        res=max(res,streak)
    return res

def sortAndSetSol(nums):
    sortNums=sorted(nums)
    numSet=set(sortNums)
    print(numSet)
    i=0
    longest=0
    while i<=len(nums)-1:
        long=1
        while sortNums[i]+long in numSet:
            long+=1
        i=i+long
        longest=max(long,longest)
    return longest

def efficientSol(nums):
    numSet=set(nums)
    longest=0
    for num in numSet:
        if (num-1) not in numSet:
            length=1
            while num+length in numSet:
                length+=1
            longest=max(length,longest)
    return longest
print(efficientSol([2,20,4,10,3,4,5]))
print(efficientSol([0,3,2,5,4,6,1,1]))
print(efficientSol([1,0,-1]))
print(efficientSol([1]))