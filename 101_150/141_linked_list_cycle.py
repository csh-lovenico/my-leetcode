# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        fast = head
        slow = head
        while True:
            # fast pointer moves 2 nodes
            fast = fast.next
            if fast is None:
                return False
            else:
                fast = fast.next
                if fast is None:
                    return False
            # slow pointer moves 1 node
            slow = slow.next
            if fast == slow:
                return True
