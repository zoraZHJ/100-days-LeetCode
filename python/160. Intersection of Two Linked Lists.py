# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        len1 = 0
        listA = headA
        while(listA is not None):
            listA = listA.next
            len1 += 1

        len2 = 0
        listB = headB
        while(listB is not None):
            listB = listB.next
            len2 += 1
        
        listA = headA
        listB = headB

        if len1 > len2:
            diff_len = len1 - len2
            while(diff_len > 0):
                listA = listA.next
                diff_len -= 1
        
        if len1 < len2:
            diff_len = len2 - len1
            while(diff_len > 0):
                listB = listB.next
                diff_len -= 1
        
        while(listA != listB and (listA is not None) and (listB is not None)):
            listA = listA.next
            listB = listB.next
        
        if listA == listB and listA is not None:
            return listA
        else:
            return None