def lvhDistance(str1,str2):
    n=len(str1)
    m=len(str2)
    prev=[0 for i in range(n+1)]
    curr=[0 for i in range(n+1)]
    for i in range(n+1):
        prev[i]=i;
    for i in range(1,n):
        curr[0]=i
        for j in range(1,m):
            if str1[i-1]==str2[j-1]:
                curr[j]=prev[j-1]
            else:
                curr[j]=1+min(
                    curr[j-1],
                    prev[j],
                    prev[j-1]
                )
        print("Prev", prev)
        print("Curr",curr)

        prev=curr.copy()
    print(curr)
    return curr[n]


print(lvhDistance("kitten","sitting"))