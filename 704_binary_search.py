import math
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lower = 0
        upper = len(nums) - 1
        while lower < upper:
            mid = math.floor((upper + lower + 1) / 2)
            if nums[mid] > target:
                upper = mid - 1
            if nums[mid] < target:
                lower = mid
            if nums[mid] == target:
                return mid
        if lower == upper:
            if nums[lower] == target:
                return lower
        return -1


if __name__ == '__main__':
    print(Solution().search([5], 5))
