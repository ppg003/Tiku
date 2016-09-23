"""
http://cv.qiaobutang.com/post/55c483380cf2b4db80726f3d
给定N个磁盘，每个磁盘大小为D[i],i=0...N-1,现在要在这N个磁盘上"顺序分配"M个分区，每个分区大小为P[j]，j=0....M-1。
顺序分配的意思是：分配一个分区P[j]时，如果当前磁盘剩余空间足够，则在当前磁盘分配；
如果不够，则尝试下一个磁盘，直到找到一个磁盘D[i+k]可以容纳该分区；
分配下一个分区P[j+1]时，则从当前磁盘D[i+k]的剩余空间开始分配，不在使用D[i+k]之前磁盘末分配的空间；
如果这M个分区不能在这N个磁盘完全分配，则认为分配失败，请实现函数，is_allocable判断给定N个磁盘（数组D）和M个分区（数组P），是否会出现分配失败的情况。
举例：磁盘为[120,120,120],分区为[60,60,80,20,80]可分配 ，如果为[60,80,80,20,80]则分配失败。
"""


def is_allocable(d, m):
    l_d = len(d)
    l_m = len(m)
    t_d = sum(d)
    t_m = sum(m)
    if t_m > t_d:
        return False
    i_d = 0
    i_m = 0
    while i_d < l_d and 0 < t_m < t_d:
        res = d[i_d]
        while i_m < l_m and res >= m[i_m]:
            res -= m[i_m]
            t_m -= m[i_m]
            i_m += 1
        t_d -= d[i_d]
        i_d += 1
    if t_m > 0:
        return False
    return True


d = [120, 120, 120]
m_s = [60, 60, 80, 20, 80]
m_f = [60, 80, 80, 20, 80]
print(is_allocable(d, m_s))
