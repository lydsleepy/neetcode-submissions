class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
    
    def add_word(self, word):
        curr = self
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.end = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for w in words:
            root.add_word(w)

        rows, cols = len(board), len(board[0])
        ans, visited = set(), set()

        def inBounds(r, c):
            return 0 <= r < rows and 0 <= c < cols

        def dfs(r, c, node, word):
            if not inBounds(r, c) or (r, c) in visited or board[r][c] not in node.children:
                return
            visited.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.end:
                ans.add(word)
            
            for rn, cn in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                r2, c2 = r + rn, c + cn
                if inBounds(r2, c2) and (r2, c2) not in visited:
                    dfs(r2, c2, node, word)

            visited.remove((r, c))
        
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root, "")
        
        ans = list(ans)
        return ans