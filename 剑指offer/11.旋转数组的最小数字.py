#Time: O(logn)
#Space: O(1)

#考虑的特殊情况都在测试用例中：数组为空、数组只含有一个数、数组两端相等中间相等、数组两端相等中间不等、数组两端不等
#多种情况可以按照两端是否相等合并分类讨论
#注意最后return 的位置，错过

#其它解法：暴力遍历，O(n)；排序后返回，O(nlogn)
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        length = len(rotateArray)
        if not length:
            return None
        if length == 1:
            return rotateArray[0]

        l,r = 0,length-1
        while l < r - 1:
            mid = (r+l) >> 1
            if rotateArray[l] == rotateArray[r] == rotateArray[mid]:#第一类
                return sorted(rotateArray)[0]
            elif rotateArray[l] < rotateArray[r]:#第二类
                return rotateArray[0]
            else:#第三类
                if rotateArray[mid] <= rotateArray[r]:
                    r = mid
                elif rotateArray[mid] > rotateArray[r]:
                    l = mid
        return rotateArray[r]

if __name__ == '__main__':
    s = Solution()
    a = s.minNumberInRotateArray([])
    b = s.minNumberInRotateArray([4])
    c = s.minNumberInRotateArray([0,1,1,3,5,6,7])
    d = s.minNumberInRotateArray([3,1,2,3,3,3,3,3,3])
    e = s.minNumberInRotateArray([3,0,1,2,3])
    f = s.minNumberInRotateArray([4,5,7,9,2,3])
    print(a,b,c,d,e,f)
