# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        tmpNode = node
        if (tmpNode.next!=None):
            tmpNode.val = tmpNode.next.val
            tmpNode.next = tmpNode.next.next


