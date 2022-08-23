# Definition for singly-linked list.
import heapq
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        heap = []
        for i in range(len(lists)):
            if lists[i] is not None:
                heapq.heappush(heap, (lists[i].val, i))

        head = ListNode()
        current = head
        while heap:
            min_tuple = heapq.heappop(heap)
            current.next = ListNode(min_tuple[0])
            current = current.next
            lists[min_tuple[1]] = lists[min_tuple[1]].next
            if lists[min_tuple[1]] is not None:
                heapq.heappush(heap, (lists[min_tuple[1]].val, min_tuple[1]))
        return head.next
