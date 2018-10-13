def josephus(num, k, m):
    alist = list(range(1, num + 1))
    index, step = k - 1, m  # 从1号开始报数，数到3的那个人出列
    for i in range(num-1):
        index = (index + step - 1) % len(alist)
        print('出去的数：', alist.pop(index))
    return '最后的一个数：%s' % alist[0]

print(josephus(13, 1, 3))
