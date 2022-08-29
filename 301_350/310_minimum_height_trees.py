import collections
from typing import List


# https://leetcode.com/problems/minimum-height-trees/discuss/2320379/Python3-Simple-BFS-solution-using-queue-with-comments
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # Start BFS from leaves (degree 0), add them to queue
        # On removing from queue, check its neighbors, decrease their degree by 1
        # If they become leaf now (degree 0), add them to queue
        # The process repeats till we have number of vertices left is 2 or less

        # For odd length longest path - only one vertix will be answer
        # For even length longest path - two vertices will be answer

        # to capture neighbors
        adj_list = {i: [] for i in range(n)}
        # to capture degree of each node
        degree = [0] * n

        for edge in edges:
            adj_list[edge[0]].append(edge[1])
            adj_list[edge[1]].append(edge[0])
            degree[edge[0]] += 1
            degree[edge[1]] += 1

        q = collections.deque([])
        for i in range(n):
            # If they are leaf node, add them to the queue
            if degree[i] == 1:
                q.append(i)

        while n > 2:
            # No of vertices left (total - already put on queue)
            n -= len(q)

            for i in range(len(q)):
                node = q.popleft()
                # Reduce the degree of neighbors by 1
                for neighbor in adj_list[node]:
                    degree[neighbor] -= 1
                    # If neighbor become leaf, add it to the queue
                    if degree[neighbor] == 1:
                        q.append(neighbor)

        return [q.popleft() for i in range(len(q))] if len(q) else [i for i in range(n)]