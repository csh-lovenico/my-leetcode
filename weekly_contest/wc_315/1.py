from typing import List


class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort(key=lambda x: (abs(x), x), reverse=True)
        print(nums)
        for i in range(len(nums) - 1):
            if nums[i] < 0:
                continue
            if nums[i] + nums[i + 1] == 0:
                return nums[i]

        return -1
