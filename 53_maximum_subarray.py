from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        max_sum = [0] * len(nums)
        # dp stores the max sum of this section when the i-th number is read
        dp[0] = nums[0]
        # max_sum stores the overall max sum when the i-th number is read
        max_sum[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])
            max_sum[i] = max(max_sum[i - 1], dp[i])
        return max_sum[len(nums) - 1]
