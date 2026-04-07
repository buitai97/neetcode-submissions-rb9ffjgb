from queue import Queue
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        SIZE = len(grid)
        if not grid or grid[0][0] == 1 or grid[SIZE-1][SIZE-1] == 1:
            return -1
        q = Queue()
        visited = set()
        length = 1
        q.put((0, 0))
        visited.add((0,0))
        directions = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
        
        while not q.empty():
            for i in range(q.qsize()):
                r, c = q.get()
                if r == c == SIZE-1:
                    return length
                
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if min(nc, nr) < 0 or nr == SIZE or nc == SIZE or (nr,nc) in visited or grid[nr][nc] == 1:
                        continue
                    q.put((nr, nc))
                    visited.add((nr,nc))
            length += 1
        return -1