# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # slow ptr is the middle of the list
        fast_ptr = head
        slow_ptr = head
        while True:
            fast_ptr = fast_ptr.next
            if fast_ptr is None:
                break
            else:
                fast_ptr = fast_ptr.next
                if fast_ptr is None:
                    slow_ptr = slow_ptr.next
                    break
            # slow pointer moves 1 node
            slow_ptr = slow_ptr.next

        # only one element in the list, return an empty list
        if slow_ptr == head:
            return None

        before_mid = head
        while before_mid.next != slow_ptr:
            before_mid = before_mid.next

        before_mid.next = before_mid.next.next
        return head
