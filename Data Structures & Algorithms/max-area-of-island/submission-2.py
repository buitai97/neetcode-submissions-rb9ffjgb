class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        ROWS, COLS = len(grid), len(grid[0])
        max_area = 0
        visited = set()
        def dfs(r,c):
            if min(r,c) < 0 or r >= ROWS or c >= COLS or grid[r][c] == 0 or (r,c) in visited:
                return 0
            
            area = 0
            visited.add((r,c))
            area += dfs(r + 1,c)
            area += dfs(r - 1,c)
            area += dfs(r,c + 1)
            area += dfs(r,c - 1)
            return area + 1


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]==1 and (r,c) not in visited:
                    max_area = max(max_area, dfs(r,c))
        
        return max_area
        