from typing import List


# dfs + dp
# https://leetcode.com/problems/longest-increasing-path-in-a-matrix/discuss/2467013/Pythonor-DPor-DFS-orEasy-to-understand-or-Beginner
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        dp = {}
        m, n = len(matrix), len(matrix[0])

        def dfs(i, j, oldervalue):
            if not (i in range(m)) or not (j in range(n)) or matrix[i][j] <= oldervalue:
                return 0

            if (i, j) in dp:
                return dp[(i, j)]

            dp[(i, j)] = 1 + max(dfs(i + 1, j, matrix[i][j]), dfs(i - 1, j, matrix[i][j]),
                                 dfs(i, j + 1, matrix[i][j]), dfs(i, j - 1, matrix[i][j]))
            return dp[(i, j)]

        ans = 0
        for i in range(m):
            for j in range(n):
                ans = max(ans, dfs(i, j, -1))
        return ans
