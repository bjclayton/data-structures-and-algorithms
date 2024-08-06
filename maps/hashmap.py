class Pair:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value

class MyHashMap(object):
    def __init__(self):
        self.size = 1000001
        self.map = [None] * self.size

    def _hash(self, key):
        return key % self.size

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        pair = Pair(key, value)
        hash_key = self._hash(key)

        if self.map[hash_key] is None:
            self.map[hash_key] = pair
        else:
            self.map[hash_key].value = value

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """        
        hash_key = self._hash(key)
        if self.map[hash_key] is not None:
            return self.map[hash_key].value
        return -1

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        hash_key = self._hash(key)
        if self.map[hash_key] is not None:
            self.map[hash_key] = None
            return
        return -1
    
