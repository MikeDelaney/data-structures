import pytest
from queue import Queue, Node


def test_node():
    """
    Ensure Node() is correctly constructed
    """
    node = Node(500)
    assert node.value == 500
    assert node.next_node is None


def test_enqueue_empty():
    """
    If a node is added to the back of the queue
    if the queue it empty it should become the back
    and the front of the queue. It should also not
    reference any other node
    """
    queue = Queue()
    queue.enqueue(500)
    assert queue.back.value == 500
    assert queue.back.next_node is None
    assert queue.head.value == 500
    assert queue.head.next_node is None


def test_enqueue():
    """
    If an node is added to the back of the queue
    and there is already an item in the queue then
    there it should become the back of the queue
    and the previous tail will reference the new tail
    """
    queue = Queue()
    queue.enqueue(500)
    old_back = queue.back
    queue.enqueue(600)
    assert queue.back is old_back.next_node
    assert queue.back.next_node is None
    assert queue.back.value == 600
    assert old_back.value == 500


def test_dequeue():
    """
    When an item is removed from the queue, it's value
    should be returned
    """
    queue = Queue()
    queue.enqueue(500)
    queue.enqueue(600)
    queue.enqueue(700)
    assert queue.dequeue() == 500
    assert queue.dequeue() == 600
    assert queue.dequeue() == 700


def test_dequeue_empty():
    """
    If an attempt is made to remove and item from an empty
    queue, an error should be raised
    """
    queue = Queue()
    with pytest.raises(LookupError):
        queue.dequeue()


def test_size():
    """
    The size of the queue should be accurately pollable
    """
    queue = Queue()
    queue.enqueue(500)
    queue.enqueue(600)
    queue.enqueue(700)
    assert queue.size() == 3


def test_size_empty():
    """
    The size of an empty queue should be zero
    """
    queue = Queue()
    assert queue.size() == 0
