from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        s = sum(nums)
        t = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            t[i + 1] = t[i] + nums[i]
        for i in range(len(t) - 1):
            if t[i] == s - t[i + 1]:
                return i
        return -1
