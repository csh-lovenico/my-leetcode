from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] + 1 != nums[i + 1]:
                return nums[i] + 1
        if nums[-1] != len(nums):
            return nums[-1] + 1
        return 0
