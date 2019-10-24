# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class List:
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

class Solution:
    def __init__(self, vallist1, vallist2):
        self.l1 = List(vallist1)
        self.l2 = List(vallist2)


    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        pHead = l1
        curNode1 = l1
        curNode2 = l2
        jinwei = 0
        pTail = None
        while(curNode1!= None and curNode2!=None):
            sum_tmp = int(curNode1.val + curNode2.val + jinwei)
            jinwei = int(sum_tmp/10)
            sum_cur_bit = int(sum_tmp % 10)
            curNode1.val = sum_cur_bit
            pTail = curNode1
            curNode1 = curNode1.next
            curNode2 = curNode2.next
            
        while(curNode1 != None):
            sum_tmp = curNode1.val + jinwei
            jinwei = int(sum_tmp/10)
            curNode1.val = int(sum_tmp % 10)
            pTail = curNode1
            curNode1 = curNode1.next
            if jinwei == 0:
                break            
            
        while(curNode2 != None):
            sum_tmp = curNode2.val + jinwei
            jinwei = int(sum_tmp/10)
            curNode2.val = int(sum_tmp % 10)
            pTail.next = curNode2
            pTail = curNode2 #需要将末尾一个节点缓存
            curNode2 = curNode2.next
            if jinwei == 0: #需将本次操作做完再break
                break            
            
        if jinwei!=0: #有可能两个list已经遍历结束，但是jinwei!=0, 新new的节点不能直接赋值给原来存在的节点，否则源节点会和new的节点地址相同，无法保证list连续
            node = ListNode(jinwei)
            pTail.next = node

        return pHead




    def printNodeList(self, pHead):
        curNode = pHead
        print('************')
        while(curNode != None):
            print(curNode.val)
            curNode = curNode.next

if __name__ == '__main__':
    # [2,4,3],[5,6,4]
    # [0], [7, 3]
    # [5], [5]
    # [9,8], [1]
    sln = Solution([9,8], [1])
    sln.printNodeList(sln.l1.pHead)
    res = sln.addTwoNumbers(sln.l1.pHead, sln.l2.pHead)
    sln.printNodeList(res)

        