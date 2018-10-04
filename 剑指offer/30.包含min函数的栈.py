#增加辅助栈，如果入栈元素大于最小值，辅助栈里加入最小值，反之加入该入栈值
#push和pop操作知识修改了两个栈，返回值还是在top和min中，用了return

class Solution:
    def __init__(self):
        self.stack = []
        self.assist = []
    def push(self, node):
        # write code here
        self.stack.append(node)
        if not self.assist or node < self.assist[-1]:
            self.assist.append(node)
        else:
            self.assist.append(self.assist[-1])
    def pop(self):
        # write code here
        if not self.stack or not self.assist:
            return None
        self.stack.pop()
        self.assist.pop()
    def top(self):
        # write code here
        return self.stack[-1]
    def min(self):
        # write code here
        return self.assist[-1]