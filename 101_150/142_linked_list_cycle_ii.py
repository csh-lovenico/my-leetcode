# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# https://leetcode.com/problems/linked-list-cycle-ii/discuss/2502204/Python-O(1)-constant-space-solution-(Floyd's-algorithm)
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        flag = False
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                flag = True
                break

        # here if the flag is set to true, then we first set the slow pointer to head again, and traverse from slow one step,
        # and we traverse from fast which is in the cycle by one step, both the pointers fast and slow meet at a point where the cycle of
        # the linked list begins.
        # Or, if the flag is still false, meaning that there is no cycle in the linked list, we then return None(null).

        if flag == True:
            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow
        else:
            return None
