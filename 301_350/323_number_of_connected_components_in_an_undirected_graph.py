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
        if parent == child:
            return
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


# ac, slow
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        union_set = UnionSet(n)

        for edge in edges:
            union_set.union(edge[0], edge[1])

        parent_set = set()
        for i in range(n):
            parent_set.add(union_set.get_parent(i))

        return len(parent_set)


if __name__ == '__main__':
    print(Solution().countComponents(5, [[0, 1], [0, 4], [1, 4], [2, 3]]))
