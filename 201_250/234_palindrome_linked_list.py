# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast_ptr = head
        slow_ptr = head
        left_list = []
        right_list = []
        while True:
            fast_ptr = fast_ptr.next
            if fast_ptr is None:
                slow_ptr = slow_ptr.next
                break
            else:
                fast_ptr = fast_ptr.next
                if fast_ptr is None:
                    slow_ptr = slow_ptr.next
                    break
            # slow pointer moves 1 node
            slow_ptr = slow_ptr.next

        slow_ptr2 = head
        while slow_ptr:
            left_list.append(slow_ptr2.val)
            right_list.append(slow_ptr.val)
            slow_ptr = slow_ptr.next
            slow_ptr2 = slow_ptr2.next

        right_list.reverse()
        for i in range(len(left_list)):
            if left_list[i] != right_list[i]:
                return False
        return True
