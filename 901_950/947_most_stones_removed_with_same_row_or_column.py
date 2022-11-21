from typing import List


class UnionSet:
    def __init__(self, length: int):
        self.parent = list(range(length))
        self.rank = [0] * length
        self.length = length

    def union(self, parent: int, child: int):
        parent = self.get_parent(parent)
        child = self.get_parent(child)
        parent_rank = self.rank[parent]
        child_rank = self.rank[child]
        if parent == child:
            return
        self.length -= 1
        if parent_rank > child_rank:
            self.parent[child] = parent
        elif parent_rank < child_rank:
            self.parent[parent] = child
        else:
            self.parent[child] = parent
            self.rank[parent] = self.rank[parent] + 1

    def get_parent(self, node: int):
        if node == self.parent[node]:
            return node
        else:
            self.parent[node] = self.get_parent(self.parent[node])
            return self.parent[node]


# https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/solutions/863112/simple-python-union-find-solution/
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        union_set = UnionSet(n)
        row, col = {}, {}
        for stone, (r, c) in enumerate(stones):
            # connect the stones that shares the same row
            if r not in row:
                row[r] = stone
            else:
                union_set.union(row[r], stone)
            # connect the stones sharing the same column
            if c not in col:
                col[c] = stone
            else:
                union_set.union(col[c], stone)
        # set.length is the number of stones cannot be removed -- the number of roots
        return n - union_set.length
