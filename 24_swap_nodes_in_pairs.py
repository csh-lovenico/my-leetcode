# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        prev_head = head
        new_head = head.next
        next_pair = new_head.next
        new_head.next = prev_head
        prev_head.next = self.swapPairs(next_pair)

        return new_head
