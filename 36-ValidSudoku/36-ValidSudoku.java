// Last updated: 5/26/2025, 3:30:53 PM
import java.util.*;;

class Solution {
    public boolean isValidSudoku(char[][] board) {
        Map<Integer, Set<Character>> rows = new HashMap<>();
        Map<Integer, Set<Character>> cols = new HashMap<>();
        Map<String, Set<Character>> squares = new HashMap<>();

        for (int r = 0; r < 9; r++) {
            for (int c = 0; c < 9; c++) {
                char val = board[r][c];
                if (val == ('.')) continue;
                
                rows.putIfAbsent(r, new HashSet<>());
                cols.putIfAbsent(c, new HashSet<>());
                String squareKey = (r / 3) + "," + (c / 3);
                squares.putIfAbsent(squareKey, new HashSet<>());
    
                if (rows.get(r).contains(val) ||
                    cols.get(c).contains(val) ||
                    squares.get(squareKey).contains(val))
                    return false;
                
                rows.get(r).add(val);
                cols.get(c).add(val);
                squares.get(squareKey).add(val);
            }
        }

        return true;
    }
}