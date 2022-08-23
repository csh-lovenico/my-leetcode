from typing import List


# accepted but not optimal
# see https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/discuss/2465743/Python-or-Binary-Searchor-O(logN)
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        lower = 0
        upper = len(nums) - 1
        while lower < upper:
            mid = (lower + upper + 1) // 2
            if nums[mid] <= nums[-1]:
                upper = mid - 1
            elif nums[mid] > nums[-1]:
                lower = mid

        if nums[lower + 1] > nums[lower]:
            return nums[lower]
        else:
            return nums[lower + 1]


if __name__ == '__main__':
    print(Solution().findMin([3, 4, 5]))
