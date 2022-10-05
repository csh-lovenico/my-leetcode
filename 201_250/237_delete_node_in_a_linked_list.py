# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        curr = node
        # stop at the last second element
        while curr.next.next:
            curr.val = curr.next.val
            curr = curr.next
        # manually proceed the last element
        curr.val = curr.next.val
        curr.next = None
