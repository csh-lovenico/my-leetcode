# Definition for singly-linked list.
import collections


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        hashmap = collections.defaultdict(int)
        while head:
            hashmap[head.val] += 1
            head = head.next
        new_head = ListNode()
        curr = new_head
        for k, v in hashmap.items():
            if v == 1:
                curr.next = ListNode(k)
                curr = curr.next
        return new_head.next
