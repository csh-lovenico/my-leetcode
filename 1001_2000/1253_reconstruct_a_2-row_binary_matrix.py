from typing import List


class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
        new_upper = upper
        new_lower = lower
        res = [[0] * len(colsum) for _ in range(2)]
        uncertain_col = []
        for i in range(len(colsum)):
            if colsum[i] == 2:
                res[0][i] = 1
                res[1][i] = 1
                new_upper -= 1
                new_lower -= 1
            elif colsum[i] == 0:
                continue
            elif colsum[i] == 1:
                uncertain_col.append(i)

        if new_lower < 0 or new_upper < 0:
            return []

        if new_upper + new_lower != len(uncertain_col):
            return []

        for _ in range(new_lower):
            res[1][uncertain_col[-1]] = 1
            uncertain_col.pop()
        for _ in range(new_upper):
            res[0][uncertain_col[-1]] = 1
            uncertain_col.pop()

        return res
