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
    tree.left = BSTree(3, tree)
    tree.right = BSTree(10, tree)
    tree.left.left = BSTree(1, tree.left)
    tree.left.right = BSTree(6, tree.left)
    tree.right.right = BSTree(14, tree.right)
    tree.left.right.left = BSTree(4, tree.left.right)
    tree.left.right.right = BSTree(7, tree.left.right)
    tree.right.right.left = BSTree(13, tree.right.right)
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


def test_delete_two_children_root(perfect_tree):
    tree = perfect_tree
    tree.delete(4)
    actual = [n.key for n in tree.in_order()]
    expected = [1, 2, 3, 5, 6, 7]
    assert actual == expected


def test_delete_two_children_non_root(perfect_tree):
    tree = perfect_tree
    tree.delete(2)
    actual = [n.key for n in tree.in_order()]
    expected = [1, 3, 4, 5, 6, 7]
    assert actual == expected


def test_delete_nonexistent(perfect_tree):
    tree = perfect_tree
    tree.delete(56)
    actual = [n.key for n in tree.in_order()]
    expected = [1, 2, 3, 4, 5, 6, 7]
    assert actual == expected


def test_rebalance_rotate_left():
    tree = BSTree(1)
    tree.right = BSTree(2, tree)
    tree.right.right = BSTree(3, tree.right)
    tree.rebalance()
    actual = [n.key for n in tree.breadth_first()]
    expected = [2, 1, 3]
    assert tree.depth() == 2
    assert tree.balance() == 0
    assert actual == expected


def test_rebalance_rotate_right():
    tree = BSTree(3)
    tree.left = BSTree(2, tree)
    tree.left.left = BSTree(1, tree.left)
    tree.rebalance()
    actual = [n.key for n in tree.breadth_first()]
    expected = [2, 1, 3]
    assert tree.depth() == 2
    assert tree.balance() == 0
    assert actual == expected


def test_rebalance_left_right():
    tree = BSTree(6)
    tree.left = BSTree(2, tree)
    tree.right = BSTree(7, tree)
    tree.left.left = BSTree(1, tree.left)
    tree.left.right = BSTree(4, tree.left)
    tree.left.right.left = BSTree(3, tree.left.right)
    tree.left.right.right = BSTree(5, tree.left.right)
    tree.rebalance()
    actual = [n.key for n in tree.breadth_first()]
    expected = [4, 2, 6, 1, 3, 5, 7]
    assert tree.depth() == 3
    assert tree.balance() == 0
    assert actual == expected


def test_rebalance_left_left():
    tree = BSTree(6)
    tree.left = BSTree(4, tree)
    tree.right = BSTree(7, tree)
    tree.left.left = BSTree(2, tree.left)
    tree.left.right = BSTree(5, tree.left)
    tree.left.left.left = BSTree(1, tree.left.left)
    tree.left.left.right = BSTree(3, tree.left.left)
    tree.rebalance()
    actual = [n.key for n in tree.breadth_first()]
    expected = [4, 2, 6, 1, 3, 5, 7]
    assert tree.depth() == 3
    assert tree.balance() == 0
    assert actual == expected


def tree_rebalance_right_left():
    tree = BSTree(2)
    tree.left = BSTree(1, tree)
    tree.right = BSTree(6, tree)
    tree.right.left = BSTree(4, tree.right)
    tree.right.left = BSTree(7, tree.right)
    tree.right.left.left = BSTree(3, tree.right.left)
    tree.right.left.right = BSTree(5, tree.right.left)
    tree.rebalance()
    actual = [n.key for n in tree.breadth_first()]
    expected = [4, 2, 6, 1, 3, 5, 7]
    assert tree.depth() == 3
    assert tree.balance() == 0
    assert actual == expected


def tree_rebalance_right_right():
    tree = BSTree(2)
    tree.left = BSTree(1, tree)
    tree.right = BSTree(4, tree)
    tree.right.left = BSTree(3, tree.right)
    tree.right.right = BSTree(6, tree.right)
    tree.right.right.left = BSTree(5, tree.right.right)
    tree.right.right.right = BSTree(7, tree.right.right)
    tree.rebalance()
    actual = [n.key for n in tree.breadth_first()]
    expected = [4, 2, 6, 1, 3, 5, 7]
    assert tree.depth() == 3
    assert tree.balance() == 0
    assert actual == expected


def test_insert_avl_single_right_branch():
    tree = BSTree()
    for i in xrange(1, 8):
        tree.insert(i)
    actual = [n.key for n in tree.breadth_first()]
    expected = [4, 2, 6, 1, 3, 5, 7]
    assert tree.depth() == 3
    assert tree.balance() == 0
    assert actual == expected


def test_insert_avl_single_left_branch():
    tree = BSTree()
    for i in xrange(7, 0, -1):
        tree.insert(i)
    actual = [n.key for n in tree.breadth_first()]
    expected = [4, 2, 6, 1, 3, 5, 7]
    assert tree.depth() == 3
    assert tree.balance() == 0
    assert actual == expected


def test_delete_avl(perfect_tree):
    tree = perfect_tree
    tree.delete(1)
    tree.delete(3)
    tree.delete(2)
    actual = [n.key for n in tree.breadth_first()]
    expected = [6, 4, 7, 5]
    assert tree.depth() == 3
    assert tree.balance() == 1
    assert actual == expected
    assert tree.key == 6
    assert tree.right.key == 7
    assert tree.left.key == 4
    assert tree.left.right.key == 5
