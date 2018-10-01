#注意：一定是stack2空了才装入stack1的元素，否则直接从stack2弹出就是要的结果

'''
入队：元素进栈A
出队：先判断栈B是否为空，为空则将栈A中的元素pop出来并push进栈B，再将栈B的第一个元素pop出栈，如不为空则直接从栈B中pop第一个元素出栈
分析：这样做入队的复杂度为O(1)，出队的复杂度则变为O(n)。
重点：直接用python的list实现队列，以list尾为队列首，则入队用insert，复杂度为O(n)，出队用pop，复杂度为O(1)
'''

class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    def push(self, node):
        self.stack1.append(node)
    def pop(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()