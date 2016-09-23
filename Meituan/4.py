"""
给定正整数X,定义函数A(n)=1+x+x^2+x^3+...+x^n(n为整数且>=0)，已知乘运算的时间远大于加运算，输入x,n：如何尽可能快的求出A(n)。
"""
import time


def an(x, n):
    if n == 0:
        return 1
    s = 1
    for i in range(n):
        s = x * s + 1
    return s


def an_bad(x, n):
    s = 0
    for i in range(n + 1):
        s += x ** i
    return s


start = time.clock()
print(an(2, 100000))
end = time.clock()
print("read: %f s" % (end - start))

start = time.clock()
print(an_bad(2, 100000))
end = time.clock()
print("read: %f s" % (end - start))
