import java.util.*;

class Solution {
    public int numIslands(char[][] grid) {
        boolean[][] visited = new boolean[grid.length][grid[0].length];

        int count = 0;

        for(int i=0; i<grid.length; i++) {
            for(int j=0; j<grid[0].length; j++) {
                if(!visited[i][j] && grid[i][j] == '1') {
                    count += 1;
                    bfs(i, j, visited, grid);
                }
            }
        }

        return count;
    }

    private void bfs(int x, int y, boolean[][] visited, char[][] grid) {
        int[][] directions = {{-1, 0}, {0, 1}, {1, 0}, {0, -1}};
        Deque<int[]> queue = new ArrayDeque<>();

        visited[x][y] = true;
        queue.offer(new int[]{x,y});

        while(queue.size() != 0) {
            int[] temp = queue.poll();
            int recent_x = temp[0];
            int recent_y = temp[1];

            for(int[] d : directions) {
                int next_x = recent_x + d[0];
                int next_y = recent_y + d[1];

                if(next_x >= 0 && next_y >= 0 && next_x < visited.length && next_y < visited[0].length) {
                    if(!visited[next_x][next_y] && grid[next_x][next_y] == '1') {
                        visited[next_x][next_y] = true;
                        queue.offer(new int[]{next_x, next_y});
                    }
                }
            }
        }
    }
}