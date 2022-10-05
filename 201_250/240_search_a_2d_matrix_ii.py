from typing import List


# https://leetcode.com/problems/search-a-2d-matrix-ii/discuss/2552311/Binary-Search-THE-EASIEST-TO-UNDERSTAND-APPROACH
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)

        # We start from the top right corner of the matrix.
        row = 0
        col = len(matrix[0]) - 1

        # In this way, on the bottom side, all elements are bigger than current element
        # At left side, all elements are smaller than the current element

        while row < n and col >= 0:
            mid = matrix[row][col]

            # If the element at this position is the target element we return True
            if mid == target: return True

            # If the element is smaller than this position that means, we need to go to left side of current element
            if mid > target:
                col -= 1
            # Otherwise we need to move to bottom side
            else:
                row += 1

        return False
