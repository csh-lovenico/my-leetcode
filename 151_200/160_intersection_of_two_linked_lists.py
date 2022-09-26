# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a_l = 0
        b_l = 0
        curr_a = headA
        curr_b = headB
        while curr_a:
            a_l += 1
            curr_a = curr_a.next
        while curr_b:
            b_l += 1
            curr_b = curr_b.next
        diff = abs(a_l - b_l)
        curr_a = headA
        curr_b = headB
        if a_l > b_l:
            for i in range(diff):
                curr_a = curr_a.next
        else:
            for i in range(diff):
                curr_b = curr_b.next

        while curr_b:
            if curr_a == curr_b:
                return curr_b
            curr_a = curr_a.next
            curr_b = curr_b.next
        return None
