class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        map = {}
        for num in nums:
            if num in map:
                return True
            map[num] = 1
        return False