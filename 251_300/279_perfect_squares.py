# ref:
# https://leetcode.com/problems/perfect-squares/discuss/2564983/Easy-to-Understand-Python-DP-Solution
class Solution:
    def numSquares(self, n: int) -> int:
        # similar to coin change
        sq = []
        dp = [n] * (n + 1)
        for i in range(0, n):
            if i*i <= n:
                sq.append(i * i)

        dp[0] = 0
        for i in range(1, n + 1):
            for s in sq:
                if i - s < 0:
                    break
                dp[i] = min(dp[i], 1 + dp[i - s])

        return dp[n]


if __name__ == '__main__':
    print(Solution().numSquares(13))
