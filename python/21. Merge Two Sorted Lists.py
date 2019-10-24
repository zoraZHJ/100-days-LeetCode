# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        
        res = None
        tail = None
        while (l1 is not None) and (l2 is not None):
            while((l1 is not None) and (l2 is not None) and l1.val <= l2.val):
                if res is None:
                    res = l1
                    tail = l1
                else:
                    tail.next = l1
                    tail = tail.next
                l1 = l1.next
            while((l1 is not None) and (l2 is not None) and l2.val < l1.val):
                if res is None:
                    res = l2
                    tail = l2
                else:
                    tail.next = l2
                    tail = tail.next
                l2 = l2.next
        if l1 is None and l2 is not None:
            tail.next = l2
        if l1 is not None and l2 is None:
            tail.next = l1
        return res
