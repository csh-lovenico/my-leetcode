from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # sort and count
        nums.sort()
        current_num = nums[0]
        current_count = 0
        for i in range(len(nums)):
            if nums[i] == current_num:
                current_count = current_count + 1
                if current_count >= len(nums) / 2:
                    break
            else:
                current_num = nums[i]
                current_count = 1

        return current_num

