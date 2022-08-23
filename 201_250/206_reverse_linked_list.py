# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def __init__(self):
        self.head = None

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        self.reverse(head)
        return self.head

    def reverse(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        if head.next is None:
            self.head = head
            return head
        else:
            self.reverse(head.next).next = head
            head.next = None
            return head
