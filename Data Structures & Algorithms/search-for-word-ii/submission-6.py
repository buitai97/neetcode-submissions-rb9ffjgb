class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            node = root
            for c in word:
                if c not in node.children:
                    node.children[c] = TrieNode()
                node = node.children[c]
            node.word = word
        res = []
        ROWS = len(board)
        COLS = len(board[0])
        def dfs(r ,c, node):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS:
                return         
            letter = board[r][c]
            if letter not in node.children:
                return
            nxt = node.children[letter]
            if nxt.word:
                res.append(nxt.word)
                nxt.word = None
            
            board[r][c] = "#"

            dfs(r + 1, c, nxt)
            dfs(r - 1, c, nxt)
            dfs(r, c + 1, nxt)
            dfs(r, c - 1, nxt)

            board[r][c] = letter
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root)
        return res