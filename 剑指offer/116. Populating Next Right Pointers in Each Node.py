# 解法一：找规律迭代
# Time:O(n)
# Space:O(1)
# 画图找规律，默认前一层排好，有next可以指向右侧节点
# 关键是保留每一层的最左侧节点，作为下一层遍历的迭代起点；注意一下最右侧节点

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return

        root.next = None

        cur = root
        while cur.left:
            cur.left.next = cur.right
            cur.right.next = cur.next.left if cur.next is not None else None
            tmp = cur.next
            while tmp is not None:
                tmp.left.next = tmp.right
                tmp.right.next = tmp.next.left if tmp.next is not None else None
                tmp = tmp.next
            cur = cur.left
        return root

# 解法三：遍历
# Time:O(n)
# Space:O(n)
# 类比层次遍历，队列存储。队列里正好是一层，可以串联；串联后遍历，将子节点压入队列

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return root
        queue = [root]

        while queue:
            length = len(queue)
			# 将队列中的元素串联起来
            tmp = queue[0]
            for i in range(length):
                queue[i].next = queue[i+1] if i+1 < length else None
			# 遍历队列中的每个元素，将每个元素的左右节点也放入队列中
            for _ in xrange(length):
				tmp = queue.pop(0)
				if tmp.left:
					queue.append(tmp.left)
				if tmp.right:
					queue.append(tmp.right)
        return root
