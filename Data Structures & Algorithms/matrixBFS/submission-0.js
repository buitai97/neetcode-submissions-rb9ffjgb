class Solution {
    /**
     * @param {number[][]}
     * @returns {number}
     */
    shortestPath(grid) {
        const rows = grid.length, cols = grid[0].length;
        let queue = new Queue();
        let visit = new Set();
        queue.push([0,0]);
        visit.add('0,0');
        let length = 0;
        const directions = [[0,1], [0,-1],[1,0],[-1,0]];

        while(!queue.isEmpty()){
            let size = queue.size();
            console.log(size)
            for (let i = 0; i < size; i++){
                let [r,c] = queue.pop();
                if (r === rows - 1 && c === cols - 1){
                    return length;
                }
                for (let [dr, dc] of directions){
                    let nr = dr + r, nc = dc + c;
                    if (
                        Math.min(nr, nc) < 0 ||
                        nr === rows ||
                        nc === cols ||
                        visit.has(`${nr},${nc}`) ||
                        grid[nr][nc] === 1
                    ){
                        continue;
                    }
                    queue.push([nr,nc]);
                    visit.add(`${nr},${nc}`);
                }
            }

            length += 1;
        }

        return -1;
    }
}
