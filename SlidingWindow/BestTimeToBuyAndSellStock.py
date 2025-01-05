def bf(prices):
    Max=0
    for i in range(len(prices)):
        for j in range(i+1,len(prices)):
            Max=max(prices[j]-prices[i],Max)
    return Max;



prices = [10,1,5,6,7,1]
print(bf(prices))



#Sliding window
def maxProfit(prices):
    l,r=0,1
    maxProfit=0
    while r<len(prices):
        if prices[l]<prices[r]:
            profit=prices[r]-prices[l]
            maxProfit=max(profit,maxProfit)
        else:
            l=r
        r+=1
        return maxProfit