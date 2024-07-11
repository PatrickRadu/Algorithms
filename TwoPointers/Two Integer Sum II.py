def twoPointers(arr,target):
    i=0
    j=len(arr)-1
    output=[]
    while i<j:
        if arr[i]+arr[j]==target:
            output.append(i+1)
            output.append(j+1)
            return output
        elif arr[i]+arr[j]<target:
            i+=1
        else:
            j-=1
    return -1

numbers = [1,2,3,4]
target=3
print(twoPointers(numbers,target))
