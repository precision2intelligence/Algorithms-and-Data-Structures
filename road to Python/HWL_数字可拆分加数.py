#递归的for循环中的if...break会跳出当前进入的递归函数
#标准的答案写法，一条语句调用def就可以

n, m = list(map(int,input().split(' ')))
l = []

def f(n, m, l, k):
    if m == 0:
        print(' '.join(l))
    for i in range(k, n + 1):
        if i > m:
            break
        l.append(str(i))
        f(n, m - i, l, i + 1)
        l.pop()

f(n, m, l, 1)