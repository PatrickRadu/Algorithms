def minInSortedArray(array):
    l=0
    r=len(array)-1
    res=array[0]
    while l<=r:
        if array[l]<array[r]:
            res=min(res,array[l])
            break
        m=(l+r)//2
        res=min(res,array[m])
        if array[m]>=array[l]:
            l=m+1
        else:
            r=m-1
    return res

def lowerBound(array):
    l,r,res=0,len(array)-1,0
    while(l<r):
        m=(l+r)//2
        if (array[m]<array[r]):
            r=m
        else:
            l=m+1
    return array[l]
print(lowerBound([3,4,5,6,1,2]))