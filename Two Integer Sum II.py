def twoPointers(arr,target):
    i=0
    j=len(arr)-1
    while i<j:
        if arr[i]+arr[j]==target:
            return [i+1,j+1]
        elif arr[i]+arr[j]<target:
            i=i+1
        else:
            j=j-1
    return -1

numbers = [1,2,3,4]
target=3
print(twoPointers(numbers,target))
