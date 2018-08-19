#Method1:直接递归
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
def fib3(n):
    a,b = 0,1
    for i in range(n):
        a,b = b,a+b
    return a

if __name__ == "__main__":
    n = 10
    res1 = [fib1(i) for i in range(n+1)]
    res2 = [fib2(i) for i in range(n + 1)]
    res3 = [fib3(i) for i in range(n + 1)]
    print(res1,res2,res3)
