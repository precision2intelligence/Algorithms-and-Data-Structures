'''
输入样例
5      5个用户+用户的喜好程度+3次查询+每次查询用户的范围和喜好度
1 2 3 3 5
3
1 2 1
2 4 5
3 5 3

'''
def getdown(arr, left, right, k, cmp):  # 找下界
    while(left < right):
        mid = (left + right) // 2
        if cmp(arr[mid], k):
            right = mid
        else:
            left = mid + 1
    return left


def getup(arr, left, right, k, cmp):  # 找上界
    while(left < right):
        mid = (left + right + 1) // 2
        if cmp(arr[mid], k):
            left = mid
        else:
            right = mid - 1
    return left


input()  # 输入用户数，不处理
userlist = list()
for i, v in enumerate(input().split()):
    userlist.append((i + 1, int(v)))
# 排序 主要关键字k，次要关键字用户标号
userlist.sort(key=lambda x: (x[1], x[0]))
n = len(userlist)
m = int(input())
# print(userlist)
for i in range(m):
    querylist = input()
    l, r, k = list(map(int, querylist.split()))
    # 找到k值的范围
    left = getdown(userlist, 0, len(userlist),
                   (0, k), lambda a, b: a[1] >= b[1])
    right = getup(userlist, left - 1, len(userlist) -
                  1, (0, k), lambda a, b: a[1] <= b[1])
    # 找用户标号的范围
    left2 = getdown(userlist, left, right + 1,
                    (l, 0), lambda a, b: a[0] >= b[0])
    right2 = getup(userlist, left2 - 1, right,
                   (r, 0), lambda a, b: a[0] <= b[0])
    print(right2 - left2 + 1)