from typing import List


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
