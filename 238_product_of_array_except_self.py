from typing import List


# https://leetcode.com/problems/product-of-array-except-self/discuss/2392298/Python-easy-solution-or-O(n)-or-without-division
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prefix: product before i
        prefix = []
        # suffix: product after i
        suffix = []
        result = []
        cur = 1
        for i in range(len(nums)):
            prefix.append(cur)
            cur = cur * nums[i]

        cur = 1
        for i in range(len(nums) - 1, -1, -1):
            suffix.append(cur)
            cur = cur * nums[i]
        suffix.reverse()

        # so result = prefix * suffix
        for i in range(len(nums)):
            result.append(prefix[i]*suffix[i])
        return result
