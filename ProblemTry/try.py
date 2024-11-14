def hasDuplicate(nums) -> bool:
   aparitii=set()
   for num in nums:
       if num in aparitii:
           return True
       aparitii.add(num)
   return False
nums=[1,2,3,3]
print(hasDuplicate(nums))