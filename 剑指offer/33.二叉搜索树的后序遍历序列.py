#序列的最后一个数字是根节点，所以要遍历寻找分界点i，使前面的i个数字小于根节点，后面的大于根节点
#不断递归每个子树
#可能出现只有左或右子树的情况，所以初始的时候isLeft和isRight设为True

class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if not sequence:
            return False
        if len(sequence) == 1:
            return True

        root = sequence[-1]
        i = 0
        while sequence[i] < root:
            i += 1
        j = i
        for j in range(i, len(sequence)):
            if sequence[j] < root:
                return False

        left = sequence[:i]
        right = sequence[i:len(sequence)-1]#易错，不要把根节点再划分到子区间递归了
        isLeft, isRight = True, True
        if len(left):
            isLeft = self.VerifySquenceOfBST(left)
        if len(right):
            isRight = self.VerifySquenceOfBST(right)
        return isLeft and isRight