class Solution {
    public int numIslands(char[][] grid) {
        boolean[][] visited = new boolean[grid.length][grid[0].length];

        int count = 0;

        for(int i=0; i<grid.length; i++) {
            for(int j=0; j<grid[0].length; j++) {
                if(!visited[i][j] && grid[i][j] == '1') {
                    count += 1;
                    dfs(i, j, visited, grid);
                }
            }
        }

        return count;
    }

    private void dfs(int x, int y, boolean[][] visited, char[][] grid) {
        int[][] direction = {{-1, 0}, {0, 1}, {1, 0}, {0, -1}};
        visited[x][y] = true;

        for(int d[] : direction) {
            int next_x = x + d[0];
            int next_y = y + d[1];

            if(next_x >= 0 && next_y >= 0 && next_x < visited.length && next_y < visited[0].length) {
                if(!visited[next_x][next_y] && grid[next_x][next_y] == '1') {
                    dfs(next_x, next_y, visited, grid);
                }
            }
        }
    }
}