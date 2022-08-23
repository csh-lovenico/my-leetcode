# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def mergelist(l1, l2):
            ptr = ListNode(0)
            curr = ptr
            while l1 != None and l2 != None:
                if l1.val <= l2.val:
                    curr.next = l1
                    l1 = l1.next
                else:
                    curr.next = l2
                    l2 = l2.next

                curr = curr.next

            if l1 != None:
                curr.next = l1
                l1 = l1.next
            if l2 != None:
                curr.next = l2
                l2 = l2.next

            return ptr.next

        def sortList(head):
            if head == None or head.next == None:
                return head

            temp = None
            slow = head
            fast = head
            while fast and fast.next:
                temp = slow
                slow = slow.next
                fast = fast.next.next

            temp.next = None
            l1 = sortList(head)
            l2 = sortList(slow)

            return mergelist(l1, l2)

        return sortList(head)
