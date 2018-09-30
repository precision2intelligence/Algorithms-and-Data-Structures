'''
本题的关键是反转后要找到到下一个未反转的节点，所以用tmp提前保存
pHead.next = last从左向右的*.next =表示把等号右边的变量存入左边节点的链接域。这里last初值为0，不可能写成last.next
p，p.next和Lnode都是节点的表示
最后返回头节点的指针
'''

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        if not pHead or not pHead.next:
            return pHead
        last = None   #指向上一个节点
        while pHead:
            #先用tmp保存pHead的下一个节点的信息，
            #保证单链表不会因为失去pHead节点的next而就此断裂
            tmp = pHead.next
            #保存完next，就可以让pHead的next指向last了
            pHead.next = last
            #让last，pHead依次向后移动一个节点，继续下一次的指针反转
            last = pHead
            pHead = tmp
        return last

