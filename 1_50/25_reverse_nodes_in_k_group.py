# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# https://leetcode.com/problems/reverse-nodes-in-k-group/discuss/2493388/Python-or-O(1)-or-Easily-Explained-or-Recursively
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # even if n (number of nodes) == 1 than k will be also 1
        if k == 1:
            return head

        # two pointers to get head and tails
        last: Optional[ListNode] = head
        first: Optional[ListNode] = head

        # steps to get the `k` pair we want
        steps = 1
        while steps < k:
            if last == None:
                return head
            last = last.next
            steps += 1

        # returning None shows our pair is incomplete, and we don't have to reverse the pairs
        if last == None:
            return head

        # 'cause our last node will be head when reversed
        head = last

        # reverse returns the first node (which will be the last node of the pair)
        # and that last node of the pair is connected to next pair which will be sent by `reverseKGroup`
        self.reverse(first, last).next = self.reverseKGroup(last.next, k)

        return head

    def reverse(self, first: Optional[ListNode], last: Optional[ListNode]):

        # to reverse
        prev: Optional[ListNode] = None
        current: Optional[ListNode] = first
        last: Optional[ListNode] = last.next
        temp: Optional[ListNode]

        while (current != last):
            temp = current.next
            current.next = prev
            prev = current
            current = temp

        return first
