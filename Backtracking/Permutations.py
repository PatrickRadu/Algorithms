class Solution:
    def permute(self, nums: [int]) -> [[int]]:
        res,sol=[],[]
        def backtrack():
            if len(sol)==len(nums):
                res.append(sol[:])
            for x in nums:
                if x not in sol:
                    sol.append(x)
                    backtrack()
                    sol.pop()

        backtrack()
        return res

solution=Solution()
print(solution.permute([1,2,3]))

