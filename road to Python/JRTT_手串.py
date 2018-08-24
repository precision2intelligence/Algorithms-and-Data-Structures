'''
输入样例
5 2 3  共5个珠子，最少2个不同色，3种颜色
3 1 2 3
0
2 2 3
1 2
1 3
'''

import sys
if __name__ == "__main__":
    n, m, c = sys.stdin.readline().strip('\n').split(' ')
    n = int(n)
    m = int(m)
    c = int(c)
    color = {}
    for i in range(n):
        x = sys.stdin.readline().strip('\n').split(' ')
        for subx in x[1:len(x)]:
            if subx not in color:
                color[subx] = []
                color[subx].append(i)
            else:
                color[subx].append(i)
            if i < m:
                color[subx].append(i + n)
    num = 0
    for key in color:
        value = color[key]
        value.sort()
        for i in range(1, len(value)):
            diff = value[i] - value[i - 1]
            if diff < m:
                num += 1
                break

    print(num)