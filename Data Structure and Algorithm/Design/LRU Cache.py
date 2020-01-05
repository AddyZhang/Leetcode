class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
    
class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.dict1 = dict()
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def get(self, key):
        if key in self.dict1:
            print(self.dict1)
            # node = Node(key, self.dict1[key])
            node = self.dict1[key]
            print(node)
            self._remove(node)
            self._add(node)
            return node.value
        return -1
    
    def put(self, key, value):
        if key in self.dict1:
            self._remove(self.dict1[key])
        node = Node(key, value)
        self._add(node)
        self.dict1[key] = node
        
        if len(self.dict1) > self.capacity:
            node = self.head.next
            self._remove(node)
            del self.dict1[node.key]
        
    def _remove(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev
    
    def _add(self, node):
        prev = self.tail.prev
        prev.next = node
        node.next = self.tail
        self.tail.prev = node
        node.prev = prev
