'''
首先分析思路：以为队列特性是先进先出的，而栈是属于后进先出的。

进栈：元素入队列A

出栈：判断如果队列A只有一个元素，直接出队。否则，吧队A中艺术出队并入队B，直到队A中只有一个元素，再直接出队，

为了下一次继续操作，互换队A和队B。

复杂度分析：

如果以列表尾作为队尾，直接用 append 插入新元素，复杂度为O(1)。 

再用pop去弹出队首，也就是列表第0个元素，弹出后插入到另一个队列中。第一次 pop，需要移动列表后面n-1个元素，第二次 pop，需要移动后面n-2个元素……直到最后只剩最后一个元素，直接出队。

复杂度：(n-1)+(n-2)+……+1=O(n^2)。

总结：直接用python的一个列表实现栈，以列表尾为栈首，则出栈和进栈的复杂度都为O(1)。
'''
class Stock:

    def __init__(self):

        self.queueA=[]

        self.queueB=[]

    def push(self,node):

        self.queueA.append(node)

    def pop(self):

        if len(self.queueA)==0:

            return None

        while len(self.queueA)!=1:

            self.queueB.append(self.queueA.pop(0))

        self.queueA,self.queueB=self.queueB,self.queueA#交换队列 A,B的位置，为了下一次的pop

        return self.queueB.pop()

if __name__=='__main__':

    times=5

    testList=list(range(times))

    testStock=Stock()

    for i in range(times):

        testStock.push(testList[i])

    print(testList)

    for i in range(times):

        print(testStock.pop())