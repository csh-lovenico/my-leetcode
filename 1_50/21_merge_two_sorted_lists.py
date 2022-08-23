# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1

        list1_ptr = list1
        list2_ptr = list2
        if list1.val <= list2.val:
            result_ptr = ListNode(list1.val)
            list1_ptr = list1_ptr.next
        else:
            result_ptr = ListNode(list2.val)
            list2_ptr = list2_ptr.next

        head = result_ptr

        while True:
            if list1_ptr is None:
                result_ptr.next = list2_ptr
                break
            if list2_ptr is None:
                result_ptr.next = list1_ptr
                break
            if list1_ptr.val <= list2_ptr.val:
                result_ptr.next = ListNode(list1_ptr.val)
                list1_ptr = list1_ptr.next
            else:
                result_ptr.next = ListNode(list2_ptr.val)
                list2_ptr = list2_ptr.next
            result_ptr = result_ptr.next
        return head
