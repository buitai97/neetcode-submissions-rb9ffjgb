class Solution {
    public boolean isValidSudoku(char[][] board) {
        HashMap<Integer, Set<Character>> cols = new HashMap<>();
        HashMap<Integer, Set<Character>> rows = new HashMap<>();
        HashMap<String, Set<Character>> squares = new HashMap<>(); // key = (r / 3, c / 3)

        for (int r = 0; r < 9; r ++){
            for (int c  = 0; c < 9; c++){
                char cell = board[r][c];
                if ( cell == '.'){
                    continue;
                }
                String squareKey = (r / 3) + "," + (c / 3);
                if(rows.getOrDefault(r, new HashSet<>()).contains(cell) 
                    || cols.getOrDefault(c, new HashSet<>()).contains(cell) 
                    || squares.getOrDefault(squareKey, new HashSet<>()).contains(cell)) {
                    return false;
                } 
                rows.computeIfAbsent(r, k -> new HashSet<>()).add(cell);
                cols.computeIfAbsent(c, k -> new HashSet<>()).add(cell);
                squares.computeIfAbsent(squareKey, k -> new HashSet<>()).add(cell);
            }
        }
        return true;

    }
}
