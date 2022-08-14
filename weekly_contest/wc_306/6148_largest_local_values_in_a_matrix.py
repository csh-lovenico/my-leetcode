from typing import List


class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        max_x = len(grid)
        result = [[0 for i in range(max_x-2)] for j in range(max_x-2)]
        # find_by_y = []
        # for i in range(len(grid)):
        #     current_y = []
        #     for j in range(1, max_y - 1):
        #         current_y.append(max(grid[i][j - 1], grid[i][j], grid[i][j + 1]))
        #     find_by_y.append(current_y)
        #
        # find_by_x = []
        # for i in range(1, len(find_by_y) - 1):
        #     x0 = max(find_by_y[i][0], find_by_y[i - 1][0], find_by_y[i + 1][0])
        #     if x0 == find_by_y[i][0]:
        #         find_by_x.append(find_by_y[i])
        #     elif x0 == find_by_y[i - 1][0]:
        #         find_by_x.append(find_by_y[i - 1])
        #     elif x0 == find_by_y[i + 1][0]:
        #         find_by_x.append(find_by_y[i + 1])
        #
        # return find_by_x
        for i in range(1, max_x - 1):
            for j in range(1, max_x - 1):
                result[i - 1][j - 1] = max(grid[i][j], grid[i - 1][j - 1], grid[i - 1][j], grid[i][j - 1],
                                           grid[i + 1][j + 1], grid[i][j + 1], grid[i + 1][j], grid[i + 1][j - 1],
                                           grid[i - 1][j + 1])
        return result
