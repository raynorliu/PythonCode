count = 0

def hanoi(n, x, y, z):
    '汉诺塔递归算法'
    global count
    if n == 1:  # 递归退出条件
        count += 1
        print('移动步骤:', x, '--->', z,'已进行',count,'次')
    else:

        count += 1
        hanoi(n-1, x, z, y)  # 将x上n-1个盘子借助z移动到y
        # print('移动步骤:', x, '--->', z)
        hanoi(1, x, y, z)  # 将x上最底下的盘子移动到z上
        hanoi(n-1, y, x, z)  # 将y上n-1个盘子借助x移动到z

    return count



n = int(input('请输入汉诺塔层数:'))
hanoi(n, 'x', 'y', 'z')
print('总计需要移动 %d次' % count)
