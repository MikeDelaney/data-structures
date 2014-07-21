from hashtable import HashTable
import pytest


def test_init():
    hash_table = HashTable(1024)
    assert hash_table.size == 1024
    assert len(hash_table.buckets) == 1024
    for item in hash_table.buckets:
        assert type(item) is list


def test_hash():
    hash_table = HashTable(1024)
    assert hash_table.hash('cat') == 312
    assert hash_table.hash('bullfrog') == 861
    assert hash_table.hash('areallylongstringfortesting') == 886


def test_set_invalid_type():
    hash_table = HashTable(1024)
    with pytest.raises(TypeError):
        hash_table.set(1, 'pig')


def test_set():
    hash_table = HashTable(1024)
    hash_table.set('pig', 'pig')
    assert hash_table.buckets[320][0] == ('pig', 'pig')


def test_get_missing_key():
    hash_table = HashTable(1024)
    hash_table.set('pig', 'pig')
    hash_table.set('sasquatch', 'sasquatch')
    with pytest.raises(KeyError):
        hash_table.get('dog')


def test_get_simple():
    hash_table = HashTable(1024)
    hash_table.set('pig', 'pig')
    hash_table.set('sasquatch', 'sasquatch')
    assert hash_table.get('pig') == 'pig'
    assert hash_table.get('sasquatch') == 'sasquatch'


def test_get_complete():
    hash_table = HashTable(1024)
    word_list = []
    with open('/usr/share/dict/words') as f:
        for line in f:
            word = line.rstrip()
            word_list.append(word)
            hash_table.set(word, word)
    for word in word_list:
        assert hash_table.get(word) == word
