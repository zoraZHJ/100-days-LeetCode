class ListNode:
    def __init__(self, v):
        self.val = v
        self.next = None

class List:
    def reverseList(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head
        oriHead = head.next
        head.next = None
        
        while oriHead != None:
            oriNext = oriHead.next #cache the next of the oriHead
            oriHead.next = head
            head = oriHead
            oriHead = oriNext
        return head


