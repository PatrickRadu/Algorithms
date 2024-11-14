#Brute force
def three_Integer_Sum(nums):
    output=[]
    #a set to sort the results
    res=set()
    nums.sort()
    #parsing the array with 3 different variables with different values to find
    #the ones that add to 0
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            for k in range(j+1,len(nums)):
                if nums[i]+nums[j]+nums[k]==0:
                    temp=[nums[i],nums[j],nums[k]]
                    #saving as a hashable structure so it doesnt add duplicates
                    res.add(tuple(temp))
    return [list(l) for l in res]

print(three_Integer_Sum([-1,0,1,2,-1,-4]))


def three_Integer_Sum_two_Pointers(nums):
    output=set()
    nums.sort()
    for i in range(len(nums)-1):
        l=i+1
        r=len(nums)-1
        while l<r:
            if nums[l]+nums[r]==-nums[i]:
                temp=[nums[l],nums[r],nums[i]]
                output.add(tuple(temp))
                l+=1
                r-=1
            elif nums[l]+nums[r]>-nums[i]:
                r=r-1
            else:
                l=l+1
    return [list(l) for l in output]

print(three_Integer_Sum_two_Pointers([-1,0,1,2,-1,-4]))
