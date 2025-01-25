
nums=[-4,-1,0,3,10]
i = 0
j = len(nums)-1
res=[]
while (i<=j):
    if abs(nums[i])<abs(nums[j]):
        res.append(nums[j]*nums[j])
        j=j-1
    else:
        res.append(nums[i]*nums[i])
        i+=1
res.reverse()
print(res)
