import math
from typing import List


# https://leetcode.com/problems/search-in-rotated-sorted-array/discuss/2408570/Simple-Python-BS
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lower = 0
        upper = len(nums) - 1
        while lower <= upper:
            mid = (lower + upper) // 2
            if nums[mid] == target:
                return mid
            # lower and mid are on the same side of break point
            if nums[lower] <= nums[mid]:
                # target is between lower and mid
                if nums[lower] <= target < nums[mid]:
                    upper = mid - 1
                else:
                    lower = mid + 1
            # lower is before the break point and mid is after the break point
            else:
                # target between mid and upper
                if nums[upper] >= target > nums[mid]:
                    lower = mid + 1
                else:
                    upper = mid - 1
        return -1
