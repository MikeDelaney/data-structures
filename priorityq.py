# -*- coding: utf-8 -*-

from binheap import Binheap


class Item(object):
    def __init__(self, priority, value):
        self.priority = priority
        self.value = value

    def __cmp__(self, other):
        return self.priority < other.priority


class Priorityq(Binheap):
    def insert(self, priority, value):
        self.push(Item(priority, value))

    def pop(self):
        pass

    def peek(self):
        pass
