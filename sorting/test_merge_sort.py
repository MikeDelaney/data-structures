from merge_sort import merge_sort


def test_merge_sort_int():
    test_list = [8, 1, 4, 59, 3, 7, 0]
    actual = merge_sort(test_list)
    expected = [0, 1, 3, 4, 7, 8, 59]
    assert actual == expected


def test_merge_sort_str():
    test_list = ['cat', 'artful', 'frog', 'watch', 'dig']
    actual = merge_sort(test_list)
    expected = ['artful', 'cat', 'dig', 'frog', 'watch']
    assert actual == expected


def test_merge_sort_empty():
    test_list = []
    actual = merge_sort(test_list)
    expected = []
    assert actual == expected
