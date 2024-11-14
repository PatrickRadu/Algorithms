def maxWaterBrute(nums):
    max=0
    for i,num in enumerate(nums):
        for j in range(i+1,len(nums)):
            area=min(num,nums[j]) * (j-i)
            print(num,nums[j],area,j,i)
            if (area>max):
                max=area
    return max

# print(maxWaterBrute([1,7,2,5,4,7,3,6]))


def maxWaterTwoPointers(heights):
    Max=0
    i=0
    j=len(heights)-1
    while i<j:
        if heights[i]<=heights[j]:
            area=heights[i]*(j-i)
            i+=1
            Max=max(area,Max)
        else:
            area=heights[j]*(j-i)
            j-=1
            Max = max(area, Max)
    return Max

print(maxWaterTwoPointers([1,7,2,5,4,7,3,6]))