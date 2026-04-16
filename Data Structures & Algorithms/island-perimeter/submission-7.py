class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        visit = set()
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[-1,0],[1,0],[0,1],[0,-1]]
        def dfs(r, c):
            if r not in range(ROWS) or c not in range(COLS) or grid[r][c] == 0:
                return 1
            if (r,c) in visit:
                return 0
            visit.add((r,c))
            res = 0
            for dr, dc in directions:
                nr, nc = r + dr, c + dc 
                res += dfs(nr, nc)
            return res
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j]:
                    return dfs(i,j)
        return 0
    