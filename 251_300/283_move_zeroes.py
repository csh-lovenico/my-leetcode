from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        non_zero_list = []
        for i in range(len(nums)):
            if nums[i] != 0:
                non_zero_list.append(nums[i])

        for i in range(len(non_zero_list)):
            nums[i] = non_zero_list[i]

        for i in range(len(non_zero_list), len(nums)):
            nums[i] = 0

# two pointers solution: https://leetcode.com/problems/move-zeroes/discuss/2431621/O(N)-Easy-to-understand-Python
