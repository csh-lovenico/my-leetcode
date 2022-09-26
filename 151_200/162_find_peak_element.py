import math
from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l = [-math.inf] + nums + [-math.inf]
        for i in range(1, len(nums) + 1):
            if l[i] > l[i - 1] and l[i] > l[i + 1]:
                return i - 1

    # binary search
    # https://leetcode.com/problems/find-peak-element/discuss/2565961/Intuitive-log(n)-solution-Python
    def findPeakElementBS(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
            left_val = float('-inf') if mid == 0 else nums[mid - 1]
            right_val = float('-inf') if mid == len(nums) - 1 else nums[mid + 1]

            # Maxima of the curve
            if left_val < nums[mid] and nums[mid] > right_val:
                return mid

            # Increasing section of the curve
            if left_val < nums[mid] < right_val:
                low = mid + 1
                continue

            # Decreasing section of the curve
            if left_val > nums[mid] > right_val:
                high = mid - 1
                continue

            # Minima of the curve
            low = mid + 1
        return 0
