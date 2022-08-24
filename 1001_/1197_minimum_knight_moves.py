import collections
import math


# https://leetcode.com/problems/minimum-knight-moves/discuss/386992/get-rid-of-TLE-for-python-BFS:
# bidirectional bfs
class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        if (x, y) == (0, 0): return 0

        def bfs(open_list, seen):
            open_list_new = []
            for i, j in open_list:
                for di, dj in [(1, 2), (2, 1), (1, -2), (2, -1),
                               (-1, 2), (-2, 1), (-1, -2), (-2, -1)]:
                    r, c = i + di, j + dj
                    if (r, c) not in seen and -4 < r < abs(x) + 4 and -4 < c < abs(y) + 4:
                        seen.add((r, c))
                        open_list_new.append((r, c))
            return open_list_new, seen

        d_src, d_des = 0, 0
        open_list_src, seen_src = [(0, 0)], {(0, 0)}
        open_list_des, seen_des = [(abs(x), abs(y))], {(abs(x), abs(y))}
        while True:
            if seen_src & seen_des: return d_src + d_des
            open_list_src, seen_src = bfs(open_list_src, seen_src)
            d_src += 1
            if seen_src & seen_des: return d_src + d_des
            open_list_des, seen_des = bfs(open_list_des, seen_des)
            d_des += 1


if __name__ == '__main__':
    print(Solution().minKnightMoves(209, -58))
