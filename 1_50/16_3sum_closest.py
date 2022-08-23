import math
from typing import List


# https://leetcode.com/problems/3sum-closest/discuss/2389414/Python-2-pointer-solution
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        m = math.inf
        output = 0
        for i in range(n):
            j = i + 1
            k = n - 1
            while j < k:
                x = nums[i] + nums[j] + nums[k]
                if abs(target - x) < m:
                    m = abs(target - x)
                    output = x
                if x < target:
                    j += 1
                elif x > target:
                    k -= 1
                else:
                    return target
        return output
