class WordDictionary:

    def __init__(self):
        self.root = {}

    def addWord(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node:
                node[ch] = {}
            node = node[ch]
        node["#"] = True

    def search(self, word: str) -> bool:
        node = self.root

        def dfs(i, node):
            # base case
            if not node:
                return False
            if i == len(word):
                return "#" in node

            # recursive case
            if word[i] == ".":
                for ch, d in node.items():
                    if ch != "#" and dfs(i+1, d):
                        return True
                return False
            else:
                if word[i] in node:
                    return dfs(i+1, node[word[i]])
                else:
                    return False
        
        return dfs(0, node)