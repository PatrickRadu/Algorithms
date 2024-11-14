def main(prices: list[int])->int:
    buy=prices[0]
    profit=0
    for i in range(len(prices)):
        if(prices[i]<buy):
            buy=prices[i]
        else:
            current_profit=prices[i]-buy
            profit=max(current_profit,profit)
    return profit

print(main(list([7,1,5,3,6,4])))



def dinamicProfit(prices):
    n=len(prices)
    dp=[[0 for _ in range(2)] for _ in range(n)]
    dp[0][0]=-prices[0]
    dp[0][1]=0

    for i in range(1,n):
        dp[i][0]=max(dp[i-1][0],-prices[i])
        dp[i][1]=max(dp[i-1][1],dp[i-1][0]+prices[i])
    return  max(dp[-1][0],dp[-1][1])

print(dinamicProfit(list([7,1,5,3,6,4])))