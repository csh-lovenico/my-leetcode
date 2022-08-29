from typing import List


# https://leetcode.com/problems/first-missing-positive/discuss/2484094/Amazon-%3A-100-Faster-Simple-Python-Solution-%3A-O(n)-time-O(1)-space
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        def swap(arr, i1, i2):
            temp = arr[i1]
            arr[i1] = arr[i2]
            arr[i2] = temp

        i = 0
        # find 1, 2, 3, 4 ... and put them in the right place
        while i < len(nums):
            correct = nums[i] - 1
            print(correct)
            if nums[i] > 0 and nums[i] <= len(nums) and nums[i] != nums[correct]:
                swap(nums, i, correct)
                print(nums)
            else:
                i += 1

        for i in range(0, len(nums)):
            if nums[i] != i + 1:
                return i + 1
        return len(nums) + 1


if __name__ == '__main__':
    print(Solution().firstMissingPositive([1,3,4,2]))
