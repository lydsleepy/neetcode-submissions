class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans, path = [], []

        def backtrack(start, remaining, path):
            if remaining == 0:
                ans.append(path[:])

            if remaining < 0:
                return
            
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i, remaining - nums[i], path)
                path.pop()
        
        backtrack(0, target, path)
        return ans