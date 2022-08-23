from typing import List


# https://leetcode.com/problems/maximal-square/discuss/2460875/easy-python-solution
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        def validRange(i, j):
            if 0 <= i < len(matrix) and 0 <= j < len(matrix[0]):
                return True
            else:
                return False

        if not matrix:
            return 0

        # dp[i][j]: the max area of 1s when including matrix[i][j]
        dp = [[0 for j in range(len(matrix[0]))] for i in range(len(matrix))]
        maxValue = 0

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == "0":
                    dp[i][j] = 0
                else:
                    v1 = dp[i][j - 1] if validRange(i, j - 1) else 0
                    v2 = dp[i - 1][j] if validRange(i - 1, j) else 0
                    v3 = dp[i - 1][j - 1] if validRange(i - 1, j - 1) else 0
                    dp[i][j] = min(v1, v2, v3) + 1
                    maxValue = max(maxValue, dp[i][j])

        return maxValue ** 2


if __name__ == '__main__':
    print(Solution().maximalSquare([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))