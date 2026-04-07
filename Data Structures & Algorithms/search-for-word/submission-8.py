class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])
        visited = set()
        def dfs(index, r, c):
            if index == len(word):
                return True

            if (
                r < 0 or r >= ROWS or
                c < 0 or c >= COLS or
                board[r][c] != word[index] or
                (r, c) in visited
            ):
                return False

            visited.add((r, c))

            found = (
                dfs(index + 1, r + 1, c) or
                dfs(index + 1, r - 1, c) or
                dfs(index + 1, r, c + 1) or
                dfs(index + 1, r, c - 1)
            )

            visited.remove((r, c))  # backtrack
            return found
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0]:
                    if dfs(0, r, c):
                        return True
        return False
        
            