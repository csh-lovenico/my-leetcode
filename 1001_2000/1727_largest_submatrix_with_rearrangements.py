from typing import List


# https://leetcode.com/problems/largest-submatrix-with-rearrangements/solutions/1154764/python-solution-easy-understanding-with-comments/
class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        row, col = len(matrix), len(matrix[0])
        for j in range(col):  # calculate the prefix consecutive one for each column
            for i in range(1, row):
                if matrix[i][j]:
                    matrix[i][j] += matrix[i - 1][j]
        ans = 0
        for i in range(row):  # for every row we sort the list in ascending order
            matrix[i].sort()
            for j in range(col - 1, -1, -1):
                if matrix[i][j] == 0:
                    break
                ans = max(ans, (col - j) * matrix[i][j])  # record the largest submatrix
        return ans
