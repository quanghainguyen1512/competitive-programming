# https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        _sum = l1.val + l2.val
        remember = _sum // 10
        head = ListNode(_sum % 10)
        prev = head

        while True:
            if l1.next is None and l2.next is None and remember == 0:
                break
            if l1.next:
                l1 = l1.next
            else:
                l1.val = 0
            if l2.next:
                l2 = l2.next
            else:
                l2.val = 0
            _sum = l1.val + l2.val + remember
            remember = _sum // 10
            value = _sum % 10
            cur = ListNode(value, None)
            prev.next = cur
            prev = cur
                
        return head
