from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result_head = ListNode()
        result_current = result_head

        def add(l11: Optional[ListNode], l22: Optional[ListNode], carry: int):
            nonlocal result_current
            l11_empty = l11 is None
            l22_empty = l22 is None
            if l11_empty and l22_empty and carry:
                result_current.next = ListNode(1)
                result_current = result_current.next
                return
            elif l11_empty and l22_empty:
                return
            elif l22 is None and l11:
                l11.val += carry
                carry = 0
                if l11.val >= 10:
                    l11.val %= 10
                    carry = 1
                result_current.next = ListNode(l11.val)
                result_current = result_current.next
                add(l11.next, None, carry)
            elif l11 is None and l22:
                l22.val += carry
                carry = 0
                if l22.val >= 10:
                    l22.val %= 10
                    carry = 1
                result_current.next = ListNode(l22.val)
                result_current = result_current.next
                add(l22.next, None, carry)
            else:
                l11.val += l22.val + carry
                carry = 0
                if l11.val >= 10:
                    l11.val %= 10
                    carry = 1
                result_current.next = ListNode(l11.val)
                result_current = result_current.next
                add(l11.next, l22.next, carry)

        add(l1, l2, 0)
        return result_head.next
