from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # similar to majority element
        nums.sort()
        current_num = None
        for i in range(len(nums)):
            if nums[i] == current_num:
                return True
            else:
                current_num = nums[i]
        return False

