"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from typing import Optional


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        if neighbors is not None:
            self.neighbors = neighbors
        else:
            self.neighbors = []


class Solution:
    def cloneGraph(self, node: 'Node') -> Optional[Node]:
        if node is None or node.val == 0:
            return None
        visited = []
        nodes = dict()
        queue = [node]
        # build new nodes
        while len(queue) > 0:
            head = queue.pop(0)
            if head.val in visited:
                continue
            # ↓ this if statement may be redundant
            if str(head.val) in nodes.keys():
                continue
            # ↑
            else:
                nodes[str(head.val)] = Node(head.val)
                visited.append(head.val)
                queue.extend(head.neighbors)
        visited.clear()
        queue = [node]
        # connect the nodes
        while len(queue) > 0:
            head = queue.pop(0)
            if head.val in visited:
                continue
            node_neighbors = []
            for neighbor in head.neighbors:
                node_neighbors.append(nodes[str(neighbor.val)])
            nodes[str(head.val)].neighbors = node_neighbors
            visited.append(head.val)
            queue.extend(head.neighbors)

        # it may be viable to merge the two steps
        return nodes['1']
