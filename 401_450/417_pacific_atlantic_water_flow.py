from typing import List


# https://leetcode.com/problems/pacific-atlantic-water-flow/discuss/2355008/Python-Simple-and-Easy-to-Understand-Solution
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        row = len(heights)
        col = len(heights[0])

        pacific = set()
        atlantic = set()

        def bfs(visited, x, y):

            visited.add((x, y))

            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:

                xx, yy = x + dx, y + dy
                if 0 <= xx < row and 0 <= yy < col and (xx, yy) not in visited and heights[xx][yy] >= heights[x][y]:
                    bfs(visited, xx, yy)

        for i in range(0, row):
            bfs(pacific, i, 0)
            bfs(atlantic, i, col - 1)

        for j in range(0, col):
            bfs(pacific, 0, j)
            bfs(atlantic, row - 1, j)

        return list(pacific.intersection(atlantic))

