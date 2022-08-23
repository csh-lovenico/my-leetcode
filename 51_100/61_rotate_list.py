# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        n = 0
        current = head
        while current:
            n += 1
            current = current.next

        shift = k % n
        if shift == 0:
            return head

        current = head
        before_break = head

        for _ in range(shift + 1):
            current = current.next
            
        while current:
            current = current.next
            before_break = before_break.next

        break_point = before_break.next
        before_break.next = None
        current = break_point

        while current.next:
            current = current.next

        current.next = head
        return break_point
