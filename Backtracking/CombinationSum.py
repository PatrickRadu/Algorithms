class Solution:
    def combinationSum(self, nums: [int], target: int) -> [[int]]:
        res,sol=[],[]
        n=len(nums)
        def backtrack(i,cur_sum):
            if cur_sum==target:
                res.append(sol[:])
                return
            if cur_sum > target or i == n:
                return
            backtrack(i+1,cur_sum)
            sol.append(nums[i])
            backtrack(i,nums[i]+cur_sum)
            sol.pop()
        backtrack(0,0)
        return res
solution=Solution()
print(solution.combinationSum([2,5,6,9],9))