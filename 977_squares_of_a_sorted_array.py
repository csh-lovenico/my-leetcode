import math
from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = []
        nums.sort(key=lambda n: abs(n))
        for i in range(len(nums)):
            result.append(pow(nums[i], 2))
        return result
