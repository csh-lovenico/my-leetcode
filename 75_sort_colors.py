from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        color_count = [0] * 3
        for i in range(len(nums)):
            color_count[nums[i]] += 1

        for i in range(color_count[0]):
            nums[i] = 0

        for i in range(color_count[0], color_count[0] + color_count[1]):
            nums[i] = 1

        for i in range(color_count[0] + color_count[1], len(nums)):
            nums[i] = 2
