# 判断一棵树是否为完全二叉树
# 左无、右有 ==> 返回 False
# 左无、右无 ==> 激活判断：之后所有节点都是叶节点
#  左有、右无 ==> 激活判断：之后所有节点都是叶节点        ==》   激活flag，只要右无之后都必须是叶节点
# 左有、右有 ==> 入队
import queue
def isCBTree(head):
    if not head:
        return False
    que = queue.Queue()
    que.put(head)
    flag = False                                # 是否激活判断过程
    while not que.empty():
        head = que.get()
        if head.left:
            que.put(head.left)
        if head.right:
            que.put(head.right)

    if (not head.left) and head.right:      #左空、又不空必不为CBT
        return False

    if flag:                                # 若过程激活则判断节点是否为叶节点
        if head.left or head.right:
            return False

    if not (head.left and head.right):      # 左不空、右空 | 左空、右空
        flag = True                         # 激活判断在此之后的节点必须为叶节点
    return True