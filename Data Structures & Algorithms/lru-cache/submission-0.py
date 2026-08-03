class Node:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.keys = {}
        self.dhead = Node()
        self.dtail = Node()
        self.dhead.next = self.dtail
        self.dtail.prev = self.dhead
    
    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        node.next = None
        node.prev = None
        self.keys.pop(node.key, None)
    
    def _insert_front(self, node):
        node.next = self.dhead.next
        node.prev = self.dhead
        self.dhead.next.prev = node
        self.dhead.next = node

        self.keys[node.key] = node

    def get(self, key: int) -> int:
        node = self.keys[key] if key in self.keys else None
        if node and node.next and node.prev:
            self._remove(node)
            self._insert_front(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        node = self.keys[key] if key in self.keys else None
        if node and node.next and node.prev:
            node.val = value
            self._remove(node)
            self._insert_front(node)
        else:
            node = Node(key, value)
            self._insert_front(node)
            self.keys[key] = node
            if len(self.keys) > self.capacity:
                self._remove(self.dtail.prev)