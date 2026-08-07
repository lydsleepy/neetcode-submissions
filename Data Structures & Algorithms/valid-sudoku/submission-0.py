class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # i guess you could just have 27 hashmaps
        # this will be so brute force

        if not board or not board[0]:
            return True

        # checks the rows
        for r in range(len(board)):
            temp = {}
            for c in range(len(board[0])):
                if board[r][c] != ".":
                    if board[r][c] in temp:
                        return False
                    temp[board[r][c]] = 1

        cols_maps = [{} for _ in range(len(board[0]))]

        # check the columns
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] != ".":
                    if board[r][c] in cols_maps[c]:
                        return False
                    cols_maps[c][board[r][c]] = 1
        
        grids_maps = [{} for _ in range(9)]

        # check the grids
        for r in range(len(board)):
            for c in range(len(board[0])):
                box = (r // 3) * 3 + (c // 3)
                if board[r][c] != ".":
                    if board[r][c] in grids_maps[box]:
                        return False
                    grids_maps[box][board[r][c]] = 1
        
        return True