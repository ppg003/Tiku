"""
n(1,2,3.....n)个元素有N!个不同的排列,将这n!个数按字典序排列，并编号0,1...n!-1,每个排号为其字典序的值，如n=3时，
字典排序为123,132,213,231,312,321,这6个数的字典序分别为0,1,2,3,4,5.，现给定n,请输出字典序为k 的排列(0<=k<n!)
"""


def zidianxu(k, n):
    lst = [i for i in range(1, n + 1)]
    s = ""
    while n > 0:
        poss_n = 1
        for i in range(n - 1, 0, -1):
            poss_n *= i

        num = k // poss_n
        mod = k % poss_n
        if mod == 0:
            num -= 1
            k = poss_n
        else:
            k = mod

        s += str(lst[num])
        lst.remove(lst[num])

        n -= 1
    return s


k = 3
n = 9
print(zidianxu(k, n))
