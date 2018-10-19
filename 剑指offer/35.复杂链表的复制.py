# 分三步，复制原链表结点、复制复杂指针、按奇偶拆分链表
#时间复杂度O(n),空间复杂度O(1)

# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None
class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        self.cloneNodes(pHead)
        self.connectSiblingNodes(pHead)
        return self.reconnectNodes(pHead)

    def cloneNodes(self, pHead):
        pNode = pHead
        while pNode:
            pCloned = RandomListNode(pNode.label)
            pCloned.next = pNode.next
            pNode.next = pCloned
            pNode = pCloned.next

    def connectSiblingNodes(self, pHead):
        pNode = pHead
        while pNode:
            pclone = pNode.next
            if pNode.random:
                pclone.random = pNode.random.next
            pNode = pclone.next

    def reconnectNodes(self, pHead):
        pNode = pHead
        pCloneHead = None
        pCloneNode = None
        if pNode:
            pCloneHead = pCloneNode = pNode.next
            pNode.next = pCloneNode.next
            pNode = pNode.next
        while pNode:
            pCloneNode.next, pCloneNode = pNode.next, pCloneNode.next
            pNode.next, pNode = pCloneNode.next, pNode.next
        return pCloneHead
