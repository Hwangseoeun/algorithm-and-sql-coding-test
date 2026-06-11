class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        chars = list(word)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == chars[0]:
                    if dfs(board, chars, 1, i, j):
                        return True

        return False

def dfs(board, chars, idx, x, y):
        if idx == len(chars):
            return True

        directions = [[-1,0], [0,1], [1,0], [0,-1]]

        temp = board[x][y]
        board[x][y] = "#"

        for dx, dy in directions:
            next_x = x + dx
            next_y = y + dy

            if next_x >= 0 and next_y >= 0 and next_x < len(board) and next_y < len(board[0]):
                if board[next_x][next_y] == chars[idx]:
                    if dfs(board, chars, idx+1, next_x, next_y):
                        return True
        
        board[x][y] = temp

        return False