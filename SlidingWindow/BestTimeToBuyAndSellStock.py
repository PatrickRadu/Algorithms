def bf(prices):
    Max=0
    for i in range(len(prices)):
        for j in range(i+1,len(prices)):
            Max=max(prices[j]-prices[i],Max)
    return Max;

prices = [10,8,7,5,2]
print(bf(prices))