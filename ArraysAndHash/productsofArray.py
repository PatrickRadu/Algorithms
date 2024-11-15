
def product(nums):
    out=[]
    for val in nums:
        p = 1
        for val1 in nums:
            if val !=val1:
                p=p*val1
        out.append(p)
    return out

nums = [1,2,4,6]
print(product(nums))

def efficientProduct(nums):
    res = [1] * len(nums)
    prefix = 1
    for i in range(len(nums)):
        res[i] = prefix
        prefix *= nums[i]
    postfix = 1
    for j in range(len(nums) - 1, -1, -1):
        res[j] *= postfix
        postfix *= nums[j]
    return res



