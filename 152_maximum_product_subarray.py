import math
from typing import List


# https://leetcode.com/problems/maximum-product-subarray/discuss/2420264/Easiest-O(n)-Python-Soln-w-Explanation-or-Single-Pass-or
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = nums[0]
        maxprod, minprod = ans, ans

        for i in range(1, len(nums)):
            if nums[i] < 0:
                maxprod, minprod = minprod, maxprod

            maxprod = max(nums[i], maxprod * nums[i])
            minprod = min(nums[i], minprod * nums[i])
            ans = max(ans, maxprod)

        return ans
