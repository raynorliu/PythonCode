def factorial_iteration(n):
    '阶乘迭代算法'
    result = n
    for i in range(1, n):
        result *= i
        print(result)
    return result


def factorial_recursion(n):
    '阶乘递归算法'
    if n == 1:
        return 1
    return n * factorial_recursion(n-1)


number = int(input('请输入一个正整数:'))
# result = factorial_iteration(number)
import sys
sys.setrecursionlimit(1000)
result = factorial_recursion(number)
print('%d 的阶乘是: %d' % (number, result))
