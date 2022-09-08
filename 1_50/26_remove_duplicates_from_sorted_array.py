from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        curr_num = nums[0]
        curr_place = 1
        count = 1
        for i in range(len(nums)):
            if nums[i] != curr_num:
                nums[curr_place] = nums[i]
                curr_num = nums[i]
                curr_place += 1
                count += 1
        return count
