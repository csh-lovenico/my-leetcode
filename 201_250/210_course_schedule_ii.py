from typing import List


class Solution:
    def __init__(self):
        self.pre_list = []
        self.visited = []
        self.clear = []
        self.order = []

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        self.visited = [0] * numCourses
        self.clear = [False] * numCourses
        for i in range(numCourses):
            self.pre_list.append([])
        for i in range(len(prerequisites)):
            self.pre_list[prerequisites[i][0]].append(prerequisites[i][1])
        for i in range(numCourses):
            if not self.dfs(i):
                return []
        return self.order

    def dfs(self, node: int) -> bool:
        # do not visit the nodes that has no problem
        if self.clear[node]:
            return True
        if self.visited[node] == 1:
            return False
        self.visited[node] = 1
        for item in self.pre_list[node]:
            if not self.dfs(item):
                return False
        # mark the node as not visited before return
        self.visited[node] = 0
        # mark the node is cleared, so it will not be visited again
        self.clear[node] = True
        # order of cleared nodes is the order of taking classes
        self.order.append(node)
        return True
