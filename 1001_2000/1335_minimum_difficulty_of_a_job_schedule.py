from typing import List


# https://leetcode.com/problems/minimum-difficulty-of-a-job-schedule/discuss/924611/DFS-greater-DP-Progression-with-Explanation-O(n3d)O(nd)
class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        N = len(jobDifficulty)
        if d > N:
            # not enough tasks to split into each day
            return -1
        dp = [[float("inf")] * d for _ in range(N)]
        # fill out first column based on max(jobDiffculty[0:i])
        dp[0][0] = jobDifficulty[0]
        for i in range(1, N):
            dp[i][0] = max(dp[i - 1][0], jobDifficulty[i])

        # fill out dp
        for i in range(1, N):
            for j in range(1, min(i + 1, d)):
                # i+1 is the crossed out boxes since there's not enough tasks to break up into multiple days
                # d is the right end of the dp grid
                for k in range(i):
                    # this is where we take terms that are calculated already on k,j-1 tile
                    dp[i][j] = min(dp[i][j], dp[k][j - 1] + max(jobDifficulty[k + 1:i + 1]))
                    # Note that min() is tring to get the lowest difficulty among the k possible break-ups of #tasks=i,#days=j
        return int(dp[-1][-1])
