class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, val):
        current = self.root
        for x in val:
            if x not in current.children:
                current.children[x] = TrieNode()
            current = current.children[x]
        current.endOfWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        rows = len(board)
        columns = len(board[0])
        trie = Trie()
        for x in words: trie.insert(x)
        
        res = set()
        visited = set()

        def dfs(r, c, node, word):
            if board[r][c] not in node.children:
                return
            
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.endOfWord:
                res.add(word)

            visited.add((r, c))
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < columns and (nr, nc) not in visited:
                    dfs(nr, nc, node, word)
            visited.remove((r, c))

        for r in range(rows):
            for c in range(columns):
                dfs(r, c, trie.root, "")
        
        return list(res)