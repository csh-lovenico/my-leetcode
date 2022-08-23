from typing import List


# https://leetcode.com/problems/combination-sum-iv/discuss/2418541/Python-Easy-Solution-(faster-than-99.5)
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        if not nums or target < 0:
            return 0
        nums = sorted(nums)
        dp = [0] * (target + 1)
        dp[0] = 1
        for i in range(1, target + 1):
            for num in nums:
                if num <= i:
                    dp[i] = dp[i] + dp[i - num]
                else:
                    break
        return dp[target]
