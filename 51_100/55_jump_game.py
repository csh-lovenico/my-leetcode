from typing import List


# https://leetcode.com/problems/jump-game/discuss/2441424/Python-%2B-DP
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        # dp[i]: maximum point left when arriving at the ith point
        dp = nums[:1] + [0] * n
        for i in range(1, n):
            dp[i] = max(dp[i - 1] - 1, nums[i])
            if dp[i - 1] == 0 or (dp[i] == 0 and i < n - 1):
                return False
        return True


if __name__ == '__main__':
    print(Solution().canJump([0, 2, 3]))
