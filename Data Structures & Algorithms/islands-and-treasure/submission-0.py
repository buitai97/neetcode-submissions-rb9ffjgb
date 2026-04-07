class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        q = collections.deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r,c))
        directions = [[-1,0], [1,0],[0,1],[0,-1]]
        while q:
            length = len(q)
            
            for _ in range(length):
                r, c = q.popleft()

                for dr,dc in directions:
                    nr = dr + r
                    nc = dc + c
                    if nr in range(ROWS) and nc in range(COLS) and grid[nr][nc] > grid[r][c]:
                        grid[nr][nc] = grid[r][c] + 1
                        q.append((nr, nc))
