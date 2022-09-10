from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1, 1]]
        triangle = [[1], [1, 1]]
        for _ in range(numRows - 2):
            last = triangle[-1]
            new_line = [last[j - 1] + last[j] for j in range(1, len(last))]
            triangle.append([1] + new_line + [1])
        return triangle
