from typing import List


# https://leetcode.com/problems/trapping-rain-water/discuss/2420570/Simple-python-solution-using-2-pointers
class Solution:
    def trap(self, height: List[int]) -> int:
        maxR = 0
        maxL = 0
        l, r = 0, len(height) - 1
        ans = 0
        while l < r:
            maxR = max(height[r], maxR)
            maxL = max(height[l], maxL)
            if maxL <= maxR:
                ans += maxL - height[l]
                l += 1

            elif maxR < maxL:
                ans += maxR - height[r]
                r -= 1
        return ans
