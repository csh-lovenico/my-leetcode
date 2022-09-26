import collections
from typing import List


# https://leetcode.com/problems/surrounded-regions/discuss/2558798/Simple-Python-Solution-or-Faster-than-91.5
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        ROWS = len(board)
        COLS = len(board[0])

        def dfs(r, c):
            # base case
            if (r < 0 or c < 0 or r == ROWS or c == COLS or board[r][c] != "O"):
                return
            board[r][c] = "T"
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        # 1. Capture unsurrounded regions (0 --> T)
        for r in range(ROWS):
            for c in range(COLS):
                if (board[r][c] == "O" and (r in [0, ROWS - 1] or c in [0, COLS - 1])):
                    dfs(r, c)
        # 2. Capture surrounded regions (O --> X)
        for r in range(ROWS):
            for c in range(COLS):
                if (board[r][c] == "O"):
                    board[r][c] = "X"

        # 3. Uncaptured unsurrounded region (T --> X)
        for r in range(ROWS):
            for c in range(COLS):
                if (board[r][c] == "T"):
                    board[r][c] = "O"


if __name__ == '__main__':
    print(Solution().solve([["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]]))
