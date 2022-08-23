from collections import defaultdict
from typing import List


# https://leetcode.com/problems/accounts-merge/discuss/2272407/Union-disjoint-set-or-python-95.76-Faster
# union disjoint set
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


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        union_set = UnionSet(len(accounts))
        mail_dict = {}
        for i in range(len(accounts)):
            emails = accounts[i][1:]
            for email in emails:
                if email in mail_dict:
                    union_set.union(mail_dict[email], i)
                else:
                    mail_dict[email] = i

        result = defaultdict(list)

        for k, v in mail_dict.items():
            index = union_set.get_parent(v)
            result[index].append(k)

        return [[accounts[i][0]] + sorted(emails) for i, emails in result.items()]
