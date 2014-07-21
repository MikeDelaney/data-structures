
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
        pass

    def get(self, key):
        pass
