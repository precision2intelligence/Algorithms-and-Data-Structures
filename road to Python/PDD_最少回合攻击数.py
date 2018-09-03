#贪心算法
#如果bufferedattck小于等于normalattack的两倍，那么每回合都用normalattack，回合数就是ceil(HP/normalattck)。
# 否则，bufferedattck大于normalattack的两倍。那么每两回合用一次bufferedattack。
import sys
import math
if __name__ == "__main__": # 读取第一行的n
    HP= int(sys.stdin.readline().strip())
    norm = int(sys.stdin.readline().strip())
    buff = int(sys.stdin.readline().strip())
    print(min(math.ceil(HP/norm),math.ceil(HP*2/buff)))