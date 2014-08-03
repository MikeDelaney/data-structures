# -*- coding: utf-8 -*-
class Node():
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node


class Stack():
    def __init__(self, head=None):
        self.head = head

    def push(self, data):
        """
        Adds data element to the top of the stack
        """
        if self.head is not None:
            self.head = Node(data, self.head)
        else:
            self.head = Node(data, None)

    def pop(self):
        """
        Removes data element from top of stack and returns its value
        """
        if self.head is None:
            raise LookupError
        else:
            retval = self.head.value
            self.head = self.head.next_node
            return retval
