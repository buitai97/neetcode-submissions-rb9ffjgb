class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m,n = len(board), len(board[0])
        visit = set()
        def dfs(row, col):
            
            if row not in range(m) or col not in range(n) or (row,col) in visit or board[row][col] == "X":
                return
            visit.add((row,col))
            board[row][col] = "T"
            print(board)
            dfs(row - 1, col)
            dfs(row + 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)

        for i in range(m):
            if board[i][0] == "O":
                dfs(i, 0)
            if board[i][n-1] == "O":
                dfs(i, n-1)
        for j in range(n):
            if board[0][j] == "O":
                dfs(0, j)
            if board[m-1][j] == "O":
                dfs(m-1, j)
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "T":
                    board[i][j] = "O"
        
