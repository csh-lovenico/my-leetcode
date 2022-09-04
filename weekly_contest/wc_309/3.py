from typing import List


# https://leetcode.com/problems/longest-nice-subarray/discuss/2527496/JavaC%2B%2BPython-Sliding-Window
class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        res = AND = i = 0
        for j in range(len(nums)):
            while AND & nums[j]:
                AND ^= nums[i]
                i += 1
            AND |= nums[j]
            res = max(res, j - i + 1)
        return res
