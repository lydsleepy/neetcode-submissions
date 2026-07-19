class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans, path = [], []
        
        def backtrack():
            # base case
            if len(path) == len(nums):
                ans.append(path[:]) # make a copy
                return
            # recursive case
            for i in range(len(nums)):
                if nums[i] not in path:
                    path.append(nums[i])
                    backtrack()
                    path.pop()
        
        backtrack()
        return ans