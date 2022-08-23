import math
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        column_l = []
        for i in range(len(matrix)):
            column_l.append(matrix[i][0])

        def search_column(x: int) -> int:
            upper = len(column_l) - 1
            lower = 0
            while lower < upper:
                mid = (lower + upper + 1) // 2
                if x < column_l[mid]:
                    upper = mid - 1
                else:
                    lower = mid
            return lower

        def search_row(x: int, row: List[int]) -> bool:
            lower = 0
            upper = len(row) - 1
            while lower < upper:
                mid = math.floor((upper + lower + 1) / 2)
                if row[mid] > x:
                    upper = mid - 1
                if row[mid] < x:
                    lower = mid
                if row[mid] == x:
                    return True
            if lower == upper:
                if row[lower] == x:
                    return True
            return False

        column = search_column(target)
        return search_row(target, matrix[column])
