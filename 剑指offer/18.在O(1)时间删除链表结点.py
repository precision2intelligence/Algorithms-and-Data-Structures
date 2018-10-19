#如果不是尾结点，复制后面的到待删除的位置
#如果是尾结点，判断是否只有一个节点，不是就遍历
#最后返回头指针

def deleteNode(self, pHead, Node):
    if Node == None or pHead == None:#如果头节点或者要删除的结点为空
        return
    if Node.next != None:#如果不是尾结点
        Node.val = Node.next.val
        Node.next = Node.next.next
    elif Node == pHead:  # 如果链表只有一个节点，那么就把头节点删掉就好了
        pHead.val = None
    else:#尾结点
        pNode = pHead
        while pNode.next != Node:
            pNode = pNode.next
        pNode.next = None

    return pHead
