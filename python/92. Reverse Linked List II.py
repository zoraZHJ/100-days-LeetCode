class ListNode:
    def __init__(self, v):
        self.val = v
        self.next = None
        
class Solution:
    def __init__(self, vallist):
        self.pHead = None
        idx = 0
        tailNode = None
        for v in vallist:
            node = ListNode(v)
            if idx == 0:
                self.pHead = node
                tailNode = node
            else:
                tailNode.next = node
                tailNode = node
            idx += 1
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if head == None or head.next == None or m >= n or m<1:
            return head
        curNode = head
        prevHead = curNode
        for idx in range(2, m+1):
            prevHead = curNode
            curNode = curNode.next
            if curNode == None:
                return head
        nextNode = curNode.next
        revHead = curNode
        revHead.next = None
        revEnd = curNode
        
        curNode = nextNode
        for idx in range(m, n):
            if curNode == None:
                return head
            print("-1-",idx, curNode.val)
            nextNode = curNode.next
            curNode.next = revHead
            revHead = curNode
            curNode = nextNode
        revEnd.next = nextNode
        print(prevHead.val)
        print(revHead.val)
        if m != 1:
            prevHead.next = revHead
        else:
            head = revHead

        return head
    
    def printNodeList(self, pHead):
        curNode = pHead
        print('************')
        while(curNode != None):
            print(curNode.val)
            curNode = curNode.next

if __name__ == '__main__':
    #[1,2,3,4,5], 2, 4
    #[3,5], 1, 2
    slt = Solution([1,2,3,4,5])
    slt.printNodeList(slt.pHead)
    pHead = slt.reverseBetween(slt.pHead, 2, 4)
    slt.printNodeList(pHead)


