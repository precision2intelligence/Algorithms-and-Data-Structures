class TreeNode():
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
def function(root):
    A = []
    result = []
    if not root:
        return result
    A.append(root)
    while A:
        current_root = A.pop(0)
        result.append(current_root.val)
        if current_root.left:
            A.append(current_root.left)
        if current_root.right:
            A.append(current_root.right)
    return result
