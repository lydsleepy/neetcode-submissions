from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        def inBounds(r, c):
            return 0 <= r < len(grid) and 0 <= c < len(grid[0])

        q = deque()
        visited = set()

        # getting the starting rotted oranges
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    q.append((r, c, 0))
                    visited.add((r, c))
        
        ans = 0
        while q:
            r, c, m = q.popleft()
            directions = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
            for r2, c2 in directions:
                if inBounds(r2, c2) and (r2, c2) not in visited and grid[r2][c2] == 1:
                    q.append((r2, c2, m + 1))
                    visited.add((r2, c2))
                    grid[r2][c2] = 2
            ans = max(ans, m)
        
        for row in grid:
            if 1 in row:
                return -1
        
        return ans