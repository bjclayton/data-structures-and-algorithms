class Node:
    def __init__(self, key=None):
        self.key = key
        self.next = None

class MyHashSet(object):
    def __init__(self):
        self.size = 1000001
        self.buckets = [None] * self.size

    def _hash(self, key):
        return key % self.size

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        hash_key = self._hash(key)
        node = Node(key)

        if self.buckets[hash_key] is None:
            self.buckets[hash_key] = node
        else:
            current = self.buckets[hash_key]
            while current:
                if current.key == key:
                    return
                if current.next is None:
                    break
            current.next = node

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        hash_key = self._hash(key)
        current = self.buckets[hash_key]

        if not current:
            return
        
        if current.key == key:
            self.buckets[hash_key] = current.next
        else:
            prev = current
            current = current.next
            while current:
                if current.key == key:
                    prev.next = current.next
                    return
                prev = current
                current = current.next

    def contains(self, key):
        """
        :type key: int
        :rtype: bool
        """
        hash_key = self._hash(key)
        current = self.buckets[hash_key]

        while current:
            if current.key == key:
                return True
            current = current.next
        return False
    