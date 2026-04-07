class Solution {
    /**
     * @param {number[][]} grid
     * @returns {number}
     */
    countPaths(grid) {
        return this.dfs(grid,0 ,0 ,new Set());
    }

    dfs(grid, r, c, visit){
        const cols = grid[0].length;
        const rows = grid.length;
        if (c < 0 || r < 0 || visit.has(`${r},${c}`) || r >= rows || c >= cols || grid[r][c] === 1){
            return 0;
        }
        if (c === cols - 1 && r === rows - 1){
            return 1;
        }
        visit.add(`${r},${c}`);

        let count = 0;
        count += this.dfs(grid, r + 1, c, visit);
        count += this.dfs(grid, r, c + 1, visit);
        count += this.dfs(grid, r - 1, c, visit);
        count += this.dfs(grid, r, c - 1, visit);

        visit.delete(`${r},${c}`);

        return count;
    }

    
}
