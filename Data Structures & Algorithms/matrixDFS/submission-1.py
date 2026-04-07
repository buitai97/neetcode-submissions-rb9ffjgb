class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        def dfs(grid, row, col, visited):
            if min(row, col) < 0 or row >= len(grid) or col >= len(grid[0]) or (row, col) in visited or grid[row][col]==1:
                return 0
            if row == len(grid)-1 and col == len(grid[0])-1:
                return 1
            visited.add((row, col))
            count = 0
            count += dfs(grid, row+1, col, visited)
            count += dfs(grid, row-1, col, visited)
            count += dfs(grid, row, col+1, visited)
            count += dfs(grid, row, col-1, visited)

            visited.remove((row, col))
            return count

        return dfs(grid, 0,0, set())
        