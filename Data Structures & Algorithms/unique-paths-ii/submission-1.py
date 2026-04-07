class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        visited = {}
        def dfs(r,c):
            if r not in range(m) or c not in range(n) or obstacleGrid[r][c] == 1:
                return 0
            
            if (r,c) in visited:
                return visited[(r,c)]

            if r == m-1 and c == n-1:
                return 1

            
            visited[(r,c)] = dfs(r + 1, c) + dfs(r, c + 1)
            return visited[(r,c)]

        return dfs(0,0)
            