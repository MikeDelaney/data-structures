import pytest
from queue import Queue, Node


def test_enqueue_empty():
    """
    If a node is added to the back of the queue
    if the queue it empty it should become the back
    and the front of the queue. It should also not
    reference any other node
    """
    pass


def test_enqueue():
    """
    If an node is added to the back of the queue
    and there is already an item in the queue then
    there it should become the back of the queue
    and the previous tail will reference the new tail
    """
    pass


def test_dequeue():
    """
    When an item is removed from the queue, it's value
    should be returned
    """
    pass


def test_dequeue_empty():
    """
    If an attempt is made to remove and item from an empty
    queue, an error should be raised
    """
    pass


def test_size():
    """
    The size of the queue should be accurately pollable
    """
    pass


def test_size_empty():
    """
    The size of an empty queue should be zero
    """
    pass
