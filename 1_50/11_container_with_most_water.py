from typing import List


# https://leetcode.com/problems/container-with-most-water/discuss/1069746/JS-Python-Java-C%2B%2B-or-2-Pointer-Solution-w-Visual-Explanation-or-beats-100
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        answer = 0
        while left < right:
            answer = max(((right - left) * min(height[right], height[left])), answer)
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        return answer


if __name__ == '__main__':
    print(Solution().maxArea([2, 1]))
