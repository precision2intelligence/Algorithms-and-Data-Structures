#Sum All Odd Fibonacci Numbers

# Given a positive integer num, return the sum of all odd Fibonacci numbers that
# are less than or equal to num.
#
# The first two numbers in the Fibonacci sequence are 1 and 1.
# Every additional number in the sequence is the sum of the two previous numbers.
# The first six numbers of the Fibonacci sequence are 1, 1, 2, 3, 5 and 8.
#
# For example, sumFibs(10) should return 10 because
#  all odd Fibonacci numbers less than 10 are 1, 1, 3, and 5.


#斐波那契数列 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233……

def sum_fibs(num):
    sequence = [1, 1]
    res = 2
    fib = 2

    while fib <= num:
        if fib % 2 != 0:
            res += fib
        fib = sequence[len(sequence) - 1] + sequence[len(sequence) - 2]
        sequence.append(fib)

    return res

result = sum_fibs(1)
print(result)