class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    INITIAL_CAPACITY = 50

    def __init__(self):
        self.capacity = HashTable.INITIAL_CAPACITY
        self.size = 0
        self.buckets = [None] * self.capacity

    def hash(self, key):
        hash_sum = 0

        for idx, c in enumerate(key):
            hash_sum += (idx + len(key)) ** ord(c)
            hash_sum = hash_sum % self.capacity

        return hash_sum

    def insert(self, key, value):
        self.size += 1
        idx = self.hash(key)
        node = self.buckets[idx]
        new_node = Node(key, value)

        if node is None:
            self.buckets[idx] = new_node
            return

        while node.next:
            node = node.next
        node.next = new_node

    def find(self, key):
        idx = self.hash(key)
        node = self.buckets[idx]

        while node is not None and node.key != key:
            node = node.next

        if node is None:
            return None

        return node.value

    def remove(self, key):
        idx = self.hash(key)
        node = self.buckets[idx]

        prev = None
        while node is not None and node.key != key:
            prev = node
            node = node.next

        if node is None:
            return None

        self.size -= 1
        result = node.value
        if prev is None:
            if node.next:
                node = node.next
                self.buckets[idx] = node
            else:
                self.buckets[idx] = None
        else:
            prev.next = node.next
            node = None

        return result
