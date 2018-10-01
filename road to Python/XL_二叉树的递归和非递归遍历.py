#后序遍历，要记录Marknode
#本质是利用栈的思想存储，后进先出

class TreeNode():
    def __init__(self,data):
        # write code here
        self.data = data
        self.left = None
        self.right = None

def pre_order(node):
    if node:
        print(node.data)
        pre_order(node.left)
        pre_order(node.right)
        return

def mid_order(node):
    if node:
        mid_order(node.left)
        print(node.data)
        mid_order(node.right)
    return

def post_order(node):
    if node:
        post_order(node.left)
        post_order(node.right)
        print(node.data)
    return

def non_recursion_pre_order(node):
    """
    1. 利用栈，对每一个结点，先输入结点内容；
    2. 若右子树不为空，右子树压栈；
    3. 若左子树不为空，左子树压栈。
    """
    if node:
        stack = [node]
        while stack:
            node = stack.pop()
            print(node.data)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
    return

def non_recursion_mid_order(node):
    stack = []
    while stack or node:#让循环进行下去，stack非空和node非空
        if node:
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            print(node.data)
            node = node.right
    return

def non_recursion_post_order(node):
    stack = []
    marknode = None
    while stack or node:
        if node:
            stack.append(node)
            node = node.left
        elif stack[-1].right != marknode:
            stack.append(stack[-1].right)
            marknode = None
        else:
            marknode = stack.pop()
            print(marknode.data)
    return

if __name__ =='__main__':
    node = TreeNode(1)
    node.left = TreeNode(2)
    node.left.left = TreeNode(3)
    node.left.right = TreeNode(4)
    node.right = TreeNode(5)
    node.right.right = TreeNode(6)
    print( "递归前序遍历:")
    pre_order(node)
    print( "非递归前序遍历:")
    non_recursion_pre_order(node)
    print("递归中序遍历:")
    mid_order(node)
    print( "非递归中序遍历:")
    non_recursion_mid_order(node)
    print("递归后序遍历:")
    post_order(node)
    print( "非递归后序遍历:")
    non_recursion_post_order(node)


