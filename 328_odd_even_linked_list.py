# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# https://leetcode.com/problems/odd-even-linked-list/discuss/2428188/Very-fast-and-easy-python-solution-beats-99-using-2-pointers.
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head1 = odd = ListNode()
        head2 = even = ListNode()
        t = head
        i = 0
        while t:
            if i % 2 == 0:
                even.next = t
                even = even.next
            else:
                odd.next = t
                odd = odd.next
            t = t.next
            i += 1
        odd.next = None
        even.next = head1.next
        return head2.next
