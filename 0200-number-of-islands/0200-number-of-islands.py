from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        row_len, column_len = len(grid), len(grid[0])
        direction = [[0,1], [-1,0], [0,-1], [1,0]]
        visited = [[False] * column_len for _ in range(row_len)]

        def bfs(grid, row, column):
            nonlocal count, visited

            q = deque()
            q.append((row, column))
            visited[row][column] = True

            while q:
                current_r, current_c = q.popleft()

                for dr, dc in direction:
                    next_r = current_r + dr
                    next_c = current_c + dc

                    if 0 <= next_r < row_len and 0 <= next_c < column_len and grid[next_r][next_c] == "1":
                        if not visited[next_r][next_c]:
                            q.append((next_r, next_c))
                            visited[next_r][next_c] = True

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(grid[i][j] == "1" and not visited[i][j]):
                    count += 1
                    bfs(grid, i, j)
        
        return count
        