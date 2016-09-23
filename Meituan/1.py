"""
一组随机排列的字母数组。请编写一个时间复杂度为O(n)的算法，使得这些字母按照字母从小到大顺序排好。

说明：字母区分大小写，相同的字母，排序后小写排在大写前。

例如：R，B，B，b，W，W，B，R，B，w
排序为：b，B，B，B，B，R，R，w，W，W
1)描述思路(2分)
2)请用你熟悉的编程语言编码实现(8分)
"""


def get_order(letters):
    lowcase = [0 for i in range(26)]
    upcase = [0 for i in range(26)]
    res = []
    for letter in letters:
        if "a" <= letter <= "z":
            i = ord(letter) - ord("a")
            lowcase[i] += 1
        else:
            i = ord(letter) - ord("A")
            upcase[i] += 1

    for i in range(26):
        if lowcase[i] > 0:
            res.extend(list(chr(i + ord("a")) * lowcase[i]))
        if upcase[i] > 0:
            res.extend(list(chr(i + ord("A")) * upcase[i]))
    return res


x = ["R", "B", "B", "b", "W", "W", "B", "R", "B", "w"]
print(get_order(x))
