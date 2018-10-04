#Time: O(m+n)
#Space: O(1)

#看链表定义，是单链表，没有考虑有环的情况
#思路是先计算两个链表的长度，如果不同，长链表的指针先走abs(m-n)步，这样同时到达公共结点
#计算长度的函数要好好理解下，为什么直接return而不是加1
#有公共结点的单链表，是Y字型的
#如果用栈的思想，空间复杂度是O(m+n),offer上有讲解

# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    #计算第一个结点主程序
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        m,n = self.GetLength(pHead1),self.GetLength(pHead2)
        if m > n:
            for i in range(m-n):
                pHead1 = pHead1.next
            while pHead1 != pHead2 and pHead1 and pHead2:
                pHead1 = pHead1.next
                pHead2 = pHead2.next
            return pHead1
        else:
            for i in range(n-m):
                p.Head2 = pHead2.next
            while pHead1 != pHead2 and pHead1 and pHead2:
                pHead1 = pHead1.next
                pHead2 = pHead2.next
            return pHead1
    #统计链表长度
    def GetLength(self,pHead):
        if not pHead:
            return 0
        count = 0
        while pHead:
            pHead = pHead.next
            count += 1
        return count

