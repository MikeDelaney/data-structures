
class HashTable(object):
    def __init__(self, size):
        self.size = size
        self.buckets = [[] for i in xrange(size)]

    def hash(self, key):
        hashval = 0
        for letter in key:
            hashval += ord(letter)
        return hashval % self.size

    def set(self, key, value):
        if type(key) is not str:
            raise TypeError
        self.buckets[self.hash(key)].append((key, value))

    def get(self, key):
        for kv_pair in self.buckets[self.hash(key)]:
            if key == kv_pair[0]:
                return kv_pair[1]
        raise KeyError
