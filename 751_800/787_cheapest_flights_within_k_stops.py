import collections
import sys
from typing import List


# https://leetcode.com/problems/cheapest-flights-within-k-stops/discuss/2072495/Python-or-DP-or-Memoization-or-BFSor-Multiple-Simple-Solution
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # flights[i] = [from(i), to(i), price(i)]
        min_price = [sys.maxsize] * n
        graph_dict = collections.defaultdict(list)
        for i in range(len(flights)):
            graph_dict[flights[i][0]].append([flights[i][1], flights[i][2]])
        queue = collections.deque()
        queue.append([src, 0, 0])

        while queue:
            head = queue.popleft()
            s, cost, stops = head
            if stops <= k:
                for d, c in graph_dict[s]:
                    if cost + c < min_price[d]:
                        min_price[d] = cost + c
                        queue.append([d, cost + c, stops + 1])

        if min_price[dst] < sys.maxsize:
            return int(min_price[dst])
        else:
            return -1


if __name__ == '__main__':
    print(Solution().findCheapestPrice(4, [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]], 0, 3, 1))
