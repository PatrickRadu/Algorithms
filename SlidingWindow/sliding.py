def sliding(array,k):
    l=0
    maxSum=0
    windowSum=sum(array[:k])
    for r in range(k,len(array)):
        windowSum+=array[r]-array[r-k]
        maxSum=max(maxSum,windowSum)
    return maxSum

print(sliding([1,2,3,4],2))






def longestSub(array,sum):
    maxLen=0
    l=0
    suma=0
    for r in range(len(array)):
        suma += array[r]
        if suma>sum:
            suma-=array[l]
            l+=1
        if suma==sum:
            maxLen=max(maxLen,r-l+1)
    return maxLen


print(longestSub([10,5,2,7,1,9],15))
