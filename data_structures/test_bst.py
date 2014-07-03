from bst import BSTree


def test_init_bstree():
    tree = BSTree(4)
    assert tree.key == 4
    assert tree.parent == None
    assert tree.left == None
    assert tree.right == float('inf')
    assert tree.size == 1


def test_insert_insert_already_present():
    tree = BSTree(4)
    tree.insert(4)
    assert tree.size == 1

def test_insert():
    tree = BSTree(4)
    tree.insert(2)
    tree.insert(6)
    tree.insert(1)
    tree.insert(3)
    tree.insert(5)
    tree.insert(7)
    assert tree.key == 4
    assert tree.left == 2
    assert tree.right == 6
    assert tree.left.left == 1
    assert tree.left.right == 3
    assert tree.right.left == 5
    assert tree.right.right == 7