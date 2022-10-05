from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        max_x = len(board) - 1
        max_y = len(board[0]) - 1
        live = []
        die = []

        def getState(x: int, y: int) -> int:
            if x < 0 or x > max_x or y < 0 or y > max_y:
                return 0
            return board[x][y]

        for i in range(len(board)):
            for j in range(len(board[0])):
                cnt = 0
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        if dx == 0 and dy == 0:
                            continue
                        cnt += getState(i + dx, j + dy)
                if board[i][j] == 1:
                    if cnt < 2 or cnt > 3:
                        die.append((i, j))
                if board[i][j] == 0:
                    if cnt == 2:
                        live.append((i, j))
        for x, y in live:
            board[x][y] = 1
        for x, y in die:
            board[x][y] = 0
