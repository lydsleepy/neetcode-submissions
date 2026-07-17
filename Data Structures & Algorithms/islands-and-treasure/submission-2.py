class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        def inBounds(row, col):
            return row >= 0 and col >= 0 and row < len(grid) and col < len(grid[0])
        
        visited = set()
        q = deque()
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 0:
                    q.append([row, col, 0]) # row, col, dist
                    visited.add((row, col))
        # atp: all gates are in the queue

        while q: # while queue isnt empty
            row, col, dist = q.popleft()
            neighbors = [[row + 1, col], [row - 1, col], [row, col + 1], [row, col - 1]]
            for r, c in neighbors:
                if inBounds(r, c) and grid[r][c] != -1 and (r, c) not in visited:
                    visited.add((r, c))
                    q.append([r, c, dist + 1])
                    grid[r][c] = dist + 1