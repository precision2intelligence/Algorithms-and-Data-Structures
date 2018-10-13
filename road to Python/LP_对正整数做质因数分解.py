#方法一：从最小的质数开始循环，直接判断
#注意跳出条件，是质数大于输入，因为while的过程就是找到一个质数就除尽
def fun1(n):
   res = []
   k = 2
   while k <= n:
       if n % k == 0:
           res.append(k)
           n /= k
       else:
           k += 1
   return res
print(fun1(90)) #[2, 3, 3, 5]

#方法二：先求出小于n的所有质数，是过滤法。再递归求解。
def dicprime(n):
    if n <= 1:
        return 0
    primes = [True for _ in range(n+1)]
    primes[0] = primes[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            primes[i * i:n+1:i] = [False] * len(primes[i * i:n+1:i])
    a = [i for i in range(n+1) if primes[i]]
    print(a) #所有质数[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89]
    return a
#利用递归分解n并打印质因数
def bprime(n,a,res):
    if n in a:
        res.append(n)
        return res
    else:
        x = 2
        while x <= int(n/2): #注意范围，因为从2开始的
            if n%x == 0:
                res.append(x)
                return bprime(n//x,a,res) #有点奇怪的写法，但是也好理解
            x = x + 1
def fun2(n):
    a = dicprime(n)
    return bprime(n, a, [])
print(fun2(90))
