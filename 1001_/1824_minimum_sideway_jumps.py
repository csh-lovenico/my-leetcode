from typing import List


# https://leetcode.com/problems/minimum-sideway-jumps/discuss/1152560/4-lines-Python-O(n)-Dynamic-Programming-with-detailed-explanation-and-readable-code
class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        n = len(obstacles)
        dp = [[float("inf")] * 4 for _ in range(n - 1)] + [[0] * 4]

        for i in range(n - 2, -1, -1):
            for l in {1, 2, 3} - {obstacles[i]}:
                if obstacles[i + 1] != l:
                    dp[i][l] = dp[i + 1][l]
                else:
                    for nl in {1, 2, 3} - {obstacles[i], l}:
                        dp[i][l] = min(dp[i][l], 1 + dp[i + 1][nl])

        return dp[0][2]
