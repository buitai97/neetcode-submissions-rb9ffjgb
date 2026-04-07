class Solution {
    /**
     * @param {number[][]} grid
     * @return {number}
     */
    orangesRotting(grid) {
        const q = new Queue();
        let time = 0;
        let fresh = 0;
        const rows = grid.length;
        const cols = grid[0].length;
        

        for (let r = 0; r < rows; r++){
            for (let c = 0; c < cols;c++){
                if (grid[r][c] === 1){
                    fresh += 1
                }
                if(grid[r][c] === 2){
                    q.push([r,c]);
                }
            }
        } 
        //done

        const directions = [[-1,0], [1,0],[0,-1],[0,1]]//done
        
        while(!q.isEmpty() && fresh > 0){
            const size = q.size();
            for(let i = 0; i < size;i++){
                let [r,c] = q.pop();
                for(let [dr, dc] of directions){
                    const nr = r + dr;
                    const nc = c + dc;
                    if( 
                        nr >= 0 && nr < rows &&
                        nc >= 0 &&  nc < cols &&
                        grid[nr][nc] === 1
                    ){
                        grid[nr][nc] = 2;
                        q.push([nr,nc]);
                        fresh--;
                    }
                }
            }

            time += 1;
        }

        return fresh === 0 ? time: -1;
    }
}
