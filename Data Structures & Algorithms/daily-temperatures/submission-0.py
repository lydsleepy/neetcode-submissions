class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                t, j = stack.pop()
                ans[j] = i - j
            stack.append([temp, i])
            
        return ans