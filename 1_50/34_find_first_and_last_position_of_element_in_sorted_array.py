import math
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]

        result = []

        # find first
        lower = 0
        upper = len(nums) - 1
        while lower < upper:
            mid = math.floor((upper + lower) / 2)
            if mid > len(nums) - 1:
                lower = -1
                break
            if nums[mid] >= target:
                upper = mid
            if nums[mid] < target:
                lower = mid + 1
        if nums[lower] != target:
            return [-1, -1]
        result.append(lower)

        # find last
        lower = 0
        upper = len(nums) - 1
        while lower < upper:
            mid = math.floor((upper + lower + 1) / 2)
            if mid > len(nums) - 1:
                break
            if nums[mid] > target:
                upper = mid - 1
            if nums[mid] <= target:
                lower = mid
        result.append(lower)
        return result


if __name__ == '__main__':
    print(Solution().searchRange([1, 2, 3, 3, 3, 3], 3))
