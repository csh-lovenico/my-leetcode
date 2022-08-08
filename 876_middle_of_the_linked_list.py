# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast_ptr = head
        slow_ptr = head
        while True:
            fast_ptr = fast_ptr.next
            if fast_ptr is None:
                return slow_ptr
            else:
                fast_ptr = fast_ptr.next
                if fast_ptr is None:
                    return slow_ptr.next
            # slow pointer moves 1 node
            slow_ptr = slow_ptr.next
