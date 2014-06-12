# -*- coding: utf-8 -*-

from binheap import Binheap


class Item(object):
    def __init__(self, priority, value):
        self.priority = priority
        self.value = value

    def __cmp__(self, other):
        if self.priority > other.priority:
            return 1
        elif self.priority == other.priority:
            return 0
        else:
            return -1


class Priorityq(Binheap):
    def insert(self, priority, value):
        self.push(Item(priority, value))

    def pop(self):
        super(Priorityq, self).pop()

    def peek(self):
        pass
