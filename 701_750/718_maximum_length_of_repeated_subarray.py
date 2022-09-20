from typing import List


# https://leetcode.com/problems/maximum-length-of-repeated-subarray/discuss/2599312/Python-Elegant-and-Short-or-Bottom-Up-DP
class Solution:
    def findLength(self, a: List[int], b: List[int]) -> int:
        n, m = len(a), len(b)
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(n):
            for j in range(m):
                if a[i] == b[j]:
                    dp[i + 1][j + 1] = dp[i][j] + 1

        return max(map(max, dp))
