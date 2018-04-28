def fibonacci_iteration(n):
    '迭代求菲波那锲数'
    n1 = n2 = 1
    if n < 1:
        print('输入错误')
        return -1
    elif 1 < n <= 2:
        return 1
    else:
        while(n > 2):
            n3 = n1+n2
            n1 = n2
            n2 = n3
            n -= 1
        return n3


def fibonacci_recursion(n):
    '递归求菲波那锲数'
    if n < 3:
        return 1
    return fibonacci_recursion(n-1) + fibonacci_recursion(n-2)


number = int(input('请输入需要求的n位斐波那契数'))
result = fibonacci_iteration(number)
print('第 %d 位菲波那锲数是 %d ' % (number, result))
