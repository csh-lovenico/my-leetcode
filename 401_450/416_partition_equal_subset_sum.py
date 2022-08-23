from typing import List


# dp
# https://leetcode.com/problems/partition-equal-subset-sum/discuss/2348033/Python-DP-Fast-and-Intuitive
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        total = total // 2
        # dp[i]: if the sum of subset can be i
        dp = [False] * (total + 1)
        dp[0] = True

        for num in nums:
            dp_copy = dp.copy()
            for i in range(len(dp_copy)):
                if dp_copy[i] and i + num <= total:
                    dp[i + num] = True
            if dp[total]:
                return True
        return False


if __name__ == '__main__':
    print(Solution().canPartition([1, 5, 11, 5]))
