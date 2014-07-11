from bst import BSTree
import pytest


@pytest.fixture(scope="function")
def perfect_tree():
    tree = BSTree(4)
    tree.insert(2)
    tree.insert(6)
    tree.insert(1)
    tree.insert(3)
    tree.insert(5)
    tree.insert(7)
    return tree


@pytest.fixture(scope="function")
def right_heavy():
    tree = BSTree(4)
    tree.insert(2)
    tree.insert(6)
    tree.insert(5)
    tree.insert(7)
    return tree


@pytest.fixture(scope="function")
def left_heavy():
    tree = BSTree(4)
    tree.insert(2)
    tree.insert(6)
    tree.insert(1)
    tree.insert(3)
    return tree


@pytest.fixture(scope="function")
def traverse_ex():
    tree = BSTree(8)
    tree.insert(3)
    tree.insert(10)
    tree.insert(1)
    tree.insert(6)
    tree.insert(14)
    tree.insert(4)
    tree.insert(7)
    tree.insert(13)
    return tree


def test_init_bstree():
    tree = BSTree(4)
    assert tree.key == 4
    assert tree.parent is None
    assert tree.left is None
    assert tree.right is None
    assert tree.size() == 1


def test_insert_already_present():
    tree = BSTree(4)
    tree.insert(4)
    assert tree.size() == 1


def test_insert():
    tree = BSTree(4)
    tree.insert(2)
    tree.insert(6)
    tree.insert(1)
    tree.insert(3)
    tree.insert(5)
    tree.insert(7)
    tree.insert(8)
    tree.insert(0)
    assert tree.key == 4
    assert tree.left.key == 2
    assert tree.left.parent == tree
    assert tree.right.key == 6
    assert tree.right.parent == tree
    assert tree.left.left.key == 1
    assert tree.left.left.parent == tree.left
    assert tree.left.right.key == 3
    assert tree.left.right.parent == tree.left
    assert tree.right.left.key == 5
    assert tree.right.left.parent == tree.right
    assert tree.right.right.key == 7
    assert tree.right.right.parent == tree.right
    assert tree.right.right.right.key == 8
    assert tree.left.left.left.key == 0


def test_contains_not_present(perfect_tree):
    tree = perfect_tree
    assert tree.contains(56) is False


def test_contains(perfect_tree):
    tree = perfect_tree
    assert tree.contains(1)
    assert tree.contains(2)
    assert tree.contains(3)
    assert tree.contains(4)
    assert tree.contains(5)
    assert tree.contains(6)
    assert tree.contains(7)


def test_size():
    tree = BSTree(4)
    assert tree.size() == 1
    tree.insert(2)
    assert tree.size() == 2
    tree.insert(6)
    assert tree.size() == 3
    tree.insert(1)
    assert tree.size() == 4
    tree.insert(3)
    assert tree.size() == 5
    tree.insert(5)
    assert tree.size() == 6
    tree.insert(7)
    assert tree.size() == 7


def test_depth():
    tree = BSTree(4)
    assert tree.depth() == 1
    tree.insert(2)
    assert tree.depth() == 2
    tree.insert(6)
    assert tree.depth() == 2
    tree.insert(1)
    tree.insert(3)
    tree.insert(5)
    tree.insert(7)
    assert tree.depth() == 3


def test_depth_left_heavy(left_heavy):
    tree = left_heavy
    assert tree.depth() == 3


def test_depth_right_heavy(right_heavy):
    tree = right_heavy
    assert tree.depth() == 3


def test_balance_balanced(perfect_tree):
    tree = perfect_tree
    assert tree.balance() == 0


def test_balance_left_heavy(left_heavy):
    tree = left_heavy
    assert tree.balance() == 1


def test_balance_right_heavy(right_heavy):
    tree = right_heavy
    assert tree.balance() == -1


def test_in_order(traverse_ex):
    tree = traverse_ex
    actual = [n.key for n in tree.in_order()]
    expected = [1, 3, 4, 6, 7, 8, 10, 13, 14]
    assert actual == expected


def test_in_order_perfect(perfect_tree):
    tree = perfect_tree
    actual = [n.key for n in tree.in_order()]
    expected = [1, 2, 3, 4, 5, 6, 7]
    assert actual == expected


def test_pre_order(traverse_ex):
    tree = traverse_ex
    actual = [n.key for n in tree.pre_order()]
    expected = [8, 3, 1, 6, 4, 7, 10, 14, 13]
    assert actual == expected


def test_post_order(traverse_ex):
    tree = traverse_ex
    actual = [n.key for n in tree.post_order()]
    expected = [1, 4, 7, 6, 3, 13, 14, 10, 8]
    assert actual == expected


def test_breadth_first(traverse_ex):
    tree = traverse_ex
    actual = [n.key for n in tree.breadth_first()]
    expected = [8, 3, 10, 1, 6, 14, 4, 7, 13]
    assert actual == expected


def test_delete_leaf_left(perfect_tree):
    tree = perfect_tree
    tree.delete(1)
    actual = [n.key for n in tree.in_order()]
    expected = [2, 3, 4, 5, 6, 7]
    assert actual == expected


def test_delete_leaf_right(perfect_tree):
    tree = perfect_tree
    tree.delete(3)
    actual = [n.key for n in tree.in_order()]
    expected = [1, 2, 4, 5, 6, 7]
    assert actual == expected


def test_delete_one_child_right(perfect_tree):
    tree = perfect_tree
    tree.insert(8)
    tree.delete(7)
    actual = [n.key for n in tree.in_order()]
    expected = [1, 2, 3, 4, 5, 6, 8]
    assert actual == expected


def test_delete_one_child_left(perfect_tree):
    tree = perfect_tree
    tree.insert(0)
    tree.delete(1)
    actual = [n.key for n in tree.in_order()]
    expected = [0, 2, 3, 4, 5, 6, 7]
    assert actual == expected


def test_delete_two_children():
    assert False
