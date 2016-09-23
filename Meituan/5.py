"""
http://cv.qiaobutang.com/post/55c483380cf2b4db80726f3d
已知队列支持先进先出的操作(add/remove),而栈则直技先进后出的操作push/pop,请用两个队列实现栈先进后出的操作，
希望该栈的push/pop时间复杂度尽量小。请写出push/pop的代码，需要考虑栈溢出(stackoverflow)的情况。
"""

class ListNode(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Queue(object):
    def __init__(self, maxi):
        self.head = ListNode(None)
        self.rear = self.head
        self.count = 0
        self.maxi = maxi

    def add(self, data):
        if self.count < self.maxi:
            node = ListNode(data)
            self.rear.next = node
            self.rear = node
            self.count += 1
        else:
            print("yichu")

    def remove(self):
        node = self.head.next
        self.head.next = node.next
        self.count -= 1
        return node.data

class Stack_2Q():

    def __init__(self, maxi):
        self.q1 = Queue(maxi)
        self.q2 = Queue(maxi)
        self.maxi = maxi

    def push(self, data):
        self.q1.add(data)

    def pop(self):
        pass



