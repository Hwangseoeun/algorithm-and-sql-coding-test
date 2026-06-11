class Solution {
    public boolean exist(char[][] board, String word) {
        char[] chars = word.toCharArray();

        for (int i=0; i<board.length; i++) {
            for (int j=0; j<board[0].length; j++) {
                if (board[i][j] == chars[0]) {
                    if (dfs(board, chars, 1, i, j)) {
                        return true; 
                    }
                }
            }
        }

        return false;
    }

    private boolean dfs(char[][] board, char[] chars, int idx, int x, int y) {
        if (idx == chars.length) {
            return true;
        }

        char temp = board[x][y];
        board[x][y] = '#';

        int[][] directions = {{-1,0}, {0,1}, {1,0}, {0,-1}};

        for (int[] dir : directions) {
            int nextX = x + dir[0];
            int nextY = y + dir[1];

            if (nextX >= 0 && nextY >= 0 && nextX < board.length && nextY < board[0].length) {
                if (board[nextX][nextY] == chars[idx]) {
                    if (dfs(board, chars, idx + 1, nextX, nextY)) {
                        return true;
                    }
                }
            }
        }

        board[x][y] = temp;

        return false;
    }
}