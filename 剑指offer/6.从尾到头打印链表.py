#一个有价值的错误：
#如果像列表那样，开始判断if not ListNode:  return 则报错。
#所以，链表、树这种结构的，要判断的时候要注意

# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        ans = []
        while listNode:
            ans.append(listNode.val)
            listNode = listNode.next
        return ans[::-1]