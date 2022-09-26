from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hashmap = dict()
        new_head = Node(0)
        curr_new = new_head
        curr = head
        while curr:
            curr_new.next = Node(curr.val)
            hashmap[curr] = curr_new.next
            curr = curr.next
            curr_new = curr_new.next
        curr = head
        curr_new = new_head.next
        while curr:
            if curr.random is not None:
                curr_new.random = hashmap[curr.random]
            curr = curr.next
            curr_new = curr_new.next
        return new_head.next
