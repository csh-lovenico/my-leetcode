from typing import List


# https://leetcode.com/problems/maximum-score-from-performing-multiplication-operations/discuss/2582174/Python-Solution-or-Memoization-or-Tabulation
class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        s = 0
        n = len(nums)
        m = len(multipliers)
        dp = [[0] * (m + 1) for i in range(m + 1)]
        # start from the last multiplier, move to previous one after each loop until all multipliers are used
        for j in range(m - 1, -1, -1):
            for low in range(j, -1, -1):
                # set a window at the end of num, and slide it to the first place, the size is initially 2,
                # increase the size by 1 in each loop

                # first: use the first element of the window, which means
                # the last element of the window was used in previous operation, so add dp[j + 1][low + 1]
                first = nums[low] * multipliers[j] + dp[j + 1][low + 1]
                # last: use the last element of this window, which means
                # the first element of the window was used in previous operation, so add dp[j + 1][low]
                last = nums[n - 1 - (j - low)] * multipliers[j] + dp[j + 1][low]
                print(dp[j + 1])
                print(j, low, n - 1 - (j - low), multipliers[j], dp[j + 1][low + 1], dp[j + 1][low])
                print(first, last)
                # dp[j][low]: max product of current window
                dp[j][low] = max(first, last)
        print(dp)
        return dp[0][0]


if __name__ == '__main__':
    print(Solution().maximumScore([-5, -3, -3, -2, 7, 1], [-10, -5, 3, 4, 6]))
