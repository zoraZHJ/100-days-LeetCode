# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        i = head
        j = head
        odd = False
        while(j != None):
            i = i.next
            j = j.next
            if(j != None):
                j = j.next
            else:
                odd = True
        
        k = head
        stack = []
        while(k != i):
            stack.append(k)
            k = k.next
        if odd:
            stack = stack[:-1]
        while len(stack) != 0 and stack[-1].val == k.val:
            k = k.next
            stack = stack[:-1]
        if len(stack) == 0:
            return True
        else:
            return False 
        