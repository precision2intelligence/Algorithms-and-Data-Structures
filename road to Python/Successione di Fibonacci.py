#Method1:直接递归
# Time:  O(1.618 ^ n)（1.618就是黄金分割，(1+5–√)/2）
# Space: O(n)
def fib1(n):
    if n <= 1:
        return n
    return fib1(n - 1) + fib1(n - 2)

#Method2:记忆化搜索
def fib2(n):
    memo = {0:0,1:1}
    if n not in memo:
        memo[n] = fib2(n-1) + fib2(n-2)
    return memo[n]

#Method3:迭代
# Time:  O(n)
# Space: O(1)
def fib3(n):
    a,b = 0,1
    for i in range(n):
        a,b = b,a+b
    return a

#Method4:公式法
def Fibonacci_formula(n):
    root_five = 5**0.5
    result = (((1 + root_five) / 2)**n - ((1 - root_five) / 2)**n) / root_five
    return int(result)

#Method5:迭代
# Time:  O(logn)
# Space: O(1)
from numpy import matrix

def MatrixPower(mat, n):
  assert n > 0, 'invalid n'
  res = None
  temp = mat
  while True:
    if n & 1:
      if res is None: res = temp
      else: res = res * temp
    n >>= 1
    if n == 0: break
    temp = temp * temp
  return res

def FastFibonacci(n):
  assert n >= 0, 'invalid n'
  if n < 2: return n  # F(0) = 0, F(1) = 1
  mat = matrix([[1, 1], [1, 0]], dtype=object)
  mat = MatrixPower(mat, n - 1)
  return mat[0, 0]

if __name__ == "__main__":
    n = 10
    res1 = [fib1(i) for i in range(n+1)]
    res2 = [fib2(i) for i in range(n + 1)]
    res3 = [fib3(i) for i in range(n + 1)]
    res4 = [Fibonacci_formula(i) for i in range(n + 1)]
    res5 = [FastFibonacci(i) for i in range(n+1)]
    print(res1,res2,res3,res4,res5)
