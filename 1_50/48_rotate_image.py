from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)
        if row % 2 == 0:
            upper = row // 2 -1
            lower = row // 2
        else:
            upper = row // 2 - 1
            lower = row // 2 + 1

        while upper >= 0:
            matrix[upper], matrix[lower] = matrix[lower], matrix[upper]
            upper -= 1
            lower += 1

        for i in range(row):
            for j in range(i):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp


if __name__ == '__main__':
    Solution().rotate([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]])
