#return处的判断条件可借鉴

#解法一：
#双指针，快的先走k-1步，然后快慢一起走，快的到达末尾的时候，慢的就是倒数第k个，只遍历一遍
#不太懂为什么先走k-1步而代码是k步

class Solution:
    def FindKthToTail(self, head, k):
        front,later = head,head
        i = 0
        while front:
            if i >= k:
                later = later.next
            front = front.next
            i += 1
        return later if i >= k and k >0 else None


#解法二：
#trick，用列表保存结果并返回

class Solution:
    def FindKthToTail(self, head, k):
        l = []
        node = head
        while node:
            l.append(node)
            node = node.next
        return l[-k] if k <= len(l) and k > 0 else None
