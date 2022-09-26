from typing import List


class UnionSet:
    def __init__(self, length):
        self.parent = list(range(length))
        self.rank = [0] * length

    def union(self, parent, child):
        parent = self.get_parent(parent)
        child = self.get_parent(child)
        if parent == child:
            return
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

    def getCharNum(self, c: chr):
        return ord(c) - ord('a')

    def equationsPossible(self, equations: List[str]) -> bool:
        eq_set = UnionSet(26)
        for eq in equations:
            if eq[1] == '=':
                eq_set.union(self.getCharNum(eq[0]), self.getCharNum(eq[3]))
        print(eq_set.parent)
        for eq in equations:
            if eq[1] == '!':
                if eq_set.get_parent(self.getCharNum(eq[0])) == eq_set.get_parent(self.getCharNum(eq[3])):
                    return False
        return True
