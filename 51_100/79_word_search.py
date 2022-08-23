from typing import List


# https://leetcode.com/problems/word-search/discuss/2421458/Python-simple-solution
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])

        def dfs(row, col, w):
            if w == board[row][col]:
                return True
            if board[row][col] == w[0]:
                board[row][col] = '*'
                for i, j in ((0, -1), (0, 1), (-1, 0), (1, 0)):
                    if 0 <= row + i < m and 0 <= col + j < n and board[row + i][col + j] != '*' and dfs(row + i,
                                                                                                        col + j, w[1:]):
                        return True
                board[row][col] = w[0]
            return False

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if dfs(i, j, word):
                        return True


if __name__ == '__main__':
    print(Solution().exist([["C", "A", "A"], ["A", "A", "A"], ["B", "C", "D"]], "AAB"))
