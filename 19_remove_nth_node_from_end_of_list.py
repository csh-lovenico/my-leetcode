# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return None
        first_ptr = head
        for i in range(n):
            first_ptr = first_ptr.next
        if first_ptr is None:
            return head.next
        second_ptr = head
        while first_ptr.next:
            second_ptr = second_ptr.next
            first_ptr = first_ptr.next
        second_ptr.next = second_ptr.next.next
        return head
