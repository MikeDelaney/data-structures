from quicksort import quicksort
import random


def test_quicksort_int():
    test_list = [8, 1, 4, 59, 3, 7, 0]
    actual = quicksort(test_list)
    expected = [0, 1, 3, 4, 7, 8, 59]
    assert actual == expected


def test_quicksort_int_long():
    test_list = range(1000)
    random.shuffle(test_list)
    actual = quicksort(test_list)
    expected = range(1000)
    assert actual == expected


def test_quicksort_str():
    test_list = ['cat', 'artful', 'sasquatch', 'frog', 'watch', 'dig']
    actual = quicksort(test_list)
    expected = ['artful', 'cat', 'dig', 'frog', 'sasquatch', 'watch']
    assert actual == expected


def test_quicksort_empty():
    test_list = []
    actual = quicksort(test_list)
    expected = []
    assert actual == expected
