from queue import Queue
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = Queue()
        fresh = 0
        time = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.put((r,c))
        directions = [[1,0],[0,1], [-1,0],[0,-1]]
        while fresh > 0 and  q.qsize() > 0:
            for i in range(q.qsize()):
                r,c = q.get()
                for dr, dc in directions:
                    nr,nc = dr + r, dc + c
                    if min(nr,nc) < 0 or nr >= ROWS or nc >= COLS or grid[nr][nc] == 0 or grid[nr][nc] == 2:
                        continue
                    elif grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        q.put((nr, nc))
                        print(fresh)
            time += 1
        
        return time if fresh == 0 else -1

    