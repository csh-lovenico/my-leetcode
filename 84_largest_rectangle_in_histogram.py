from typing import List


# https://leetcode.com/problems/largest-rectangle-in-histogram/discuss/2426042/Python-or-Java-O(n)-solution
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0

        # stack stores the minimum height starting from index i to the end of the list
        # example: [2, 1, 5, 6, 2, 3]
        # the minimum height from index 0 is 1, from index 2 is 2, from index 5 is 3
        stack = []

        for i in range(len(heights)):
            startIndex = i
            while stack and stack[-1][1] > heights[i]:
                print('in while')
                print(stack)
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                startIndex = index

            print('out while')
            stack.append([startIndex, heights[i]])
            print(stack)
        print(stack)

        for i in range(len(stack)):
            indx, height = stack.pop()
            maxArea = max(maxArea, height * (len(heights) - indx))

        return maxArea


if __name__ == '__main__':
    print(Solution().largestRectangleArea([2,4,5,6,5,5]))
