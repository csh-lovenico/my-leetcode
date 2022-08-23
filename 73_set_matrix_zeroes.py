from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zero_column = []
        zero_row = []
        for i in range(len(matrix)):
            p = 1
            for j in matrix[i]:
                p = p * j
                if p == 0:
                    zero_row.append(i)
                    break

        for i in range(len(matrix[0])):
            p = 1
            for j in range(len(matrix)):
                p = p * matrix[j][i]
                if p == 0:
                    zero_column.append(i)
                    break

        print(zero_column)
        print(zero_row)

        for i in zero_column:
            for j in range(len(matrix)):
                matrix[j][i] = 0
        for i in zero_row:
            for j in range(len((matrix[0]))):
                matrix[i][j] = 0

        print(matrix)


if __name__ == '__main__':
    Solution().setZeroes([[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]])
