from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_islands = 0
        queue = []
        max_x = len(grid)
        max_y = len(grid[0])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    # bfs grid[i][j]
                    queue.append((i, j))
                    while len(queue) > 0:
                        head = queue.pop(0)
                        if grid[head[0]][head[1]] == '0' or grid[head[0]][head[1]] == '-1':
                            continue
                        grid[head[0]][head[1]] = '-1'
                        if head[0] > 0:
                            queue.append((head[0] - 1, head[1]))
                        if head[1] > 0:
                            queue.append((head[0], head[1] - 1))
                        if head[0] < max_x - 1:
                            queue.append((head[0] + 1, head[1]))
                        if head[1] < max_y - 1:
                            queue.append((head[0], head[1] + 1))
                    num_islands = num_islands + 1
        return num_islands
