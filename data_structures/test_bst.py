from bst import BSTree


def test_init_bstree():
    tree = BSTree(4)
    assert tree.key == 4
    assert tree.parent == None
    assert tree.left == None
    assert tree.right == float('inf')
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
    assert tree.key == 4
    assert tree.left.key == 2
    assert tree.right.key == 6
    assert tree.left.left.key == 1
    assert tree.left.right.key == 3
    assert tree.right.left.key == 5
    assert tree.right.right.key == 7


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
    
