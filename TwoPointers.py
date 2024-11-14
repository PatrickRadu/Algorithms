# find if there exists any pair of
# elements (A[i], A[j]) such that their sum
# is equal to X.


#Metoda brute force
def isPairSum(A,N,X):
    for i in range(N):
        for j in range(N):
            if (i==j):
                continue
            if (A[i]+A[j]==X):
                return True
            if(A[i]+A[j]>X):
                break
    return 0

arr = [2, 3, 5, 8, 9, 10, 11]
val = 17

print(isPairSum(arr, len(arr), val))


#Two Pointers
def twoPointersisPairSum(A,X):
    i=0
    j=len(A)-1
    while i<j:
        if A[i]+A[j]==X:
            return True
        elif A[i]+A[j]<X:
            i+=1
        else:
            j-=1
    return 0

print(twoPointersisPairSum(arr,val))