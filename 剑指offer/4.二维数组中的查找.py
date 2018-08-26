# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        arr_row=len(array)
        arr_col=len(array[0])
        row=arr_row-1
        col=0
        flag=False
        while(row>=0 and col<arr_col):
                x=array[row][col]
                if x==target:
                    flag=True
                    break#这里别忘了跳出，不然一直循环
                elif x<target:
                    col=col+1
                else:
                    row=row-1
        return flag

if __name__=='__main__':
    find=Solution()
    target=16
    array = [[2, 3, 5], [4, 6, 8], [12, 15, 17], [14, 18, 20], [39, 40, 45]]
    aa = find.Find(target, array)
    print(aa)
