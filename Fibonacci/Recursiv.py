def rec_fibo(n):
    if(n==0):
        return 0
    if(n==1):
        return 1
    else:
        return rec_fibo(n-1)+rec_fibo(n-2)

print(rec_fibo(9))
