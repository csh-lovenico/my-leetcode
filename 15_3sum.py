from typing import List


# https://leetcode.com/problems/3sum/discuss/2398839/clean-and-concise-python-solution-easy-understanding
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort the numbers first
        nums.sort()
        result = []
        #  two pointers
        for i in range(len(nums)):
            # ignore duplicate numbers
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # put two pointers on both side of the remaining list
            left = i + 1
            right = len(nums) - 1
            while left < right:
                # compute the sum
                sum = nums[i] + nums[left] + nums[right]
                # if the sum is too large, search a smaller number
                if sum > 0:
                    right = right - 1
                # if the sum is too small, search a larger number
                elif sum < 0:
                    left = left + 1
                # if the sum is 0, output the numbers
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    left = left + 1
                    # ignore duplicate numbers
                    while nums[left] == nums[left - 1] and left < right:
                        left = left + 1
        return result
