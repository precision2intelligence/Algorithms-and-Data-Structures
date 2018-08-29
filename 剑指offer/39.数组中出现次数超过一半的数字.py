l = [7,3,5,8,5,3,5,5,5]

#解法1：排序，Python的trick
#Counter(l)是迭代器，里面是一个从大到小排序的字典
from collections import Counter
c = Counter(l)
print(c)#Counter({3: 3, 1: 2})
res = c.most_common(1)[0][0]
if l.count(res) > len(l)>>1:
    print(res)

#解法2：暴力统计，Python的trick
#一定break第一个，否则重复打印！不可能有两个都超过半数
lenth = len(l)
for i in l:
    if l.count(i)>(lenth>>1):
        print(i)
        break

#解法3:用多数冲抵少数，最后剩下的是多数。判断是否多余一般。原地处理，不改变原数组
#Time: O(n)
res = []
for d in l:
    if not res:
        res.append(d)
    else:
        if d != res[0]:
            res.pop()
        else:
            res.append(d)
if l.count(res[0]) > len(l)>>1:
    print(res[0])
    

#解法4:利用快排，找出前k个已排序数列。
#返回k的索引，即前k个已经比k小
#第k个大于长度的一半位置，即为所求
def getIndex(l,left,right):
    i,j = left,right
    if i >= j:
        return
    tar = l[i]
    while i<j:
        while i<j and l[j]>=tar:
            j -= 1
        l[i] = l[j]
        while i < j and l[i] < tar:
            i += 1
        l[j] = l[i]
    l[i] = tar
    # print(i)
    # print(l)
    return i

k = getIndex(l,0,len(l)-1)
while k != (len(l)+1)>>1:
    if k < (len(l)+1)>>1:
        k = getIndex(l,k+1,len(l)-1)
    else:
        k = getIndex(l,0,k-1)
print(l[k])



