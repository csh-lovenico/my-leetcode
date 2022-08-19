import collections
from typing import List


# https://leetcode.com/problems/shortest-path-to-get-food/discuss/2250666/Python3-oror-BFS-oror-9331
class Solution:
    def getFood(self, grid: List[List[str]]) -> int:

        rows, cols = len(grid), len(grid[0])

        for single_row in range(rows):
            for single_col in range(cols):
                if grid[single_row][single_col] == "*":
                    start = single_row, single_col
                    break

        line = collections.deque()
        initial = start, 0
        line.append(initial)
        seen = set()
        seen.add(start)

        def add_to_line(row: int, col: int, dist: int) -> None:
            nonlocal line, seen
            if (row < 0) or (row >= rows) or (col < 0) or (col >= cols) or (row, col) in seen or grid[row][col] == "X":
                return
            to_add = (row, col), dist
            seen.add((row, col))
            line.append(to_add)

        while len(line) > 0:
            cur_cord, cur_dist = line.popleft()
            r, c = cur_cord
            if grid[r][c] == "#":
                return cur_dist

            add_to_line(r + 1, c, cur_dist + 1)
            add_to_line(r - 1, c, cur_dist + 1)
            add_to_line(r, c - 1, cur_dist + 1)
            add_to_line(r, c + 1, cur_dist + 1)

        return -1
