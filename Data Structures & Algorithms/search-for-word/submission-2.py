class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])
        def dfs(index, r, c):
            if index == len(word):
                return True

            if r < 0 or r >= ROWS or c < 0 or c >= COLS:
                return False

            if board[r][c] != word[index]:
                return False

            temp = board[r][c]
            board[r][c] = "#"   # mark visited

            found = (
                dfs(index + 1, r + 1, c) or
                dfs(index + 1, r - 1, c) or
                dfs(index + 1, r, c + 1) or
                dfs(index + 1, r, c - 1)
            )

            board[r][c] = temp  # backtrack
            return found
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0]:
                    if dfs(0, r, c):
                        return True
        return False
        
            