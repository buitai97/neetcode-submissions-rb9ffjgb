class Graph {
    constructor(val) {
        this.adjList = {};
    }

    /**
     * @param {number} src
     * @param {number} dst
     * @return {void}
     */
    addEdge(src, dst) {
        if(!(src in this.adjList)){
            this.adjList[src] = new Set();
        }
        if(!(dst in this.adjList)){
            this.adjList[dst] = new Set();
        }
        this.adjList[src].add(dst);
    }

    /**
     * @param {number} src
     * @param {number} dst
     * @return {boolean}
     */
    removeEdge(src, dst) {
        if(src in this.adjList && this.adjList[src].has(dst)){
            this.adjList[src].delete(dst);
            return true;
        }
        return false
    }

    /**
     * @param {number} src
     * @param {number} dst
     * @return {boolean}
     */
    hasPath(src, dst) {
        const visited = new Set();
        return this._dfs(src, dst, visited); 
    }

    /**
     * Helper method for Depth-First Search (DFS).
     * @param {number} src - Source vertex
     * @param {number} dst - Destination vertex
     * @param {Set} visited - Set of visited vertices
     * @return {boolean} True if path exists, false otherwise
     */
    _dfs(src, dst, visited){
        if (src === dst){
            return true;
        }
        visited.add(src);
        for(const neighbor of this.adjList[src]){
            if (!visited.has(neighbor)){
                if (this._dfs(neighbor, dst, visited)){
                    return true;
                }
            }
        }
        return false;
    }
}
