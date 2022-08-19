from typing import List


class UnionSet:
    def __init__(self, length):
        self.parent = list(range(length))
        self.rank = [0] * length

    def union(self, parent, child):
        parent = self.get_parent(parent)
        child = self.get_parent(child)
        parent_rank = self.rank[parent]
        child_rank = self.rank[child]

        if parent_rank > child_rank:
            self.parent[child] = parent
        elif parent_rank < child_rank:
            self.parent[parent] = child
        else:
            self.parent[child] = parent
            self.rank[parent] = self.rank[parent] + 1

    def get_parent(self, node):
        if node == self.parent[node]:
            return node
        else:
            self.parent[node] = self.get_parent(self.parent[node])
            return self.parent[node]


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not edges:
            if n == 1:
                return True
            else:
                return False
        union_set = UnionSet(n)
        for edge in edges:
            union_set.union(edge[0], edge[1])

        for i in range(n - 1):
            if union_set.get_parent(i) != union_set.get_parent(i + 1):
                return False

        return len(edges) == n - 1
