from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = []
        max_x = len(grid)
        max_y = len(grid[0])
        minute = 0
        for i in range(max_x):
            for j in range(max_y):
                if grid[i][j] == 2:
                    queue.append((i, j, 0))
        while len(queue) > 0:
            head = queue.pop(0)
            if grid[head[0]][head[1]] == 0 or grid[head[0]][head[1]] == -1:
                continue
            if minute < head[2]:
                minute = head[2]
            grid[head[0]][head[1]] = -1
            if head[0] > 0:
                queue.append((head[0] - 1, head[1], head[2] + 1))
            if head[1] > 0:
                queue.append((head[0], head[1] - 1, head[2] + 1))
            if head[0] < max_x - 1:
                queue.append((head[0] + 1, head[1], head[2] + 1))
            if head[1] < max_y - 1:
                queue.append((head[0], head[1] + 1, head[2] + 1))

        for i in range(max_x):
            for j in range(max_y):
                if grid[i][j] == 1:
                    return -1
        return minute
