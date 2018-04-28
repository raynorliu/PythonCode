def bubble_sort(L):
    '对列表进行冒泡排序'
    _len = len(L)
    count = 0
    for i in range(_len-1, -1, -1):
        count += 1
        for j in range(i):
            count += 1
            if L[j] > L[j+1]:
                L[j], L[j+1] = L[j+1], L[j]
    print('循环次数= ', count)
    return L


def IQR(L):
    '求四分位距和4分位数'
    _L = bubble_sort(L)
    if len(L) % 2 == 0:
        print('列表为总数量为偶数,')
        (L[len(L)/2]+L[len(L)/2+1])/2


s = [5, 4, 7, 9, 8, 3, 10, 6, 1, 2]
IQR(s)
