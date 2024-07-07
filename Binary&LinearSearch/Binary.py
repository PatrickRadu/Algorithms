
array=list([1,2,3,4,5,6,7,8])

def binary_search(array,target):
    i=0
    j=len(array)-1
    while i<=j:
        mijloc=(i+j)//2
        if array[mijloc]==target:
            return mijloc
        if array[mijloc]>target:
            j=mijloc-1
        if array[mijloc]<target:
            i=mijloc+1;
    return -1;

print(binary_search(array,4))

