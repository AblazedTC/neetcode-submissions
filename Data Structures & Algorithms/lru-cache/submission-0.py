class Node:
    def __init__(self, key, val):
        self.key = key
        self.data = val
        self.prev = None
        self.nxt = None


class LRUCache:

    def __init__(self, capacity: int):
        self.head = Node(None, None)
        self.tail = Node(None, None)

        self.nodeMap = {}
        self.capacity = capacity

        self.head.nxt = self.tail
        self.tail.prev = self.head

    def remove(self, node):
        node.prev.nxt = node.nxt
        node.nxt.prev = node.prev

    def moveToFront(self, node):
        self.tail.prev.nxt = node
        node.prev = self.tail.prev
        node.nxt = self.tail
        self.tail.prev = node
        
    def get(self, key: int) -> int:
        if key not in self.nodeMap:
            return -1

        node = self.nodeMap[key]

        # remove from list
        self.remove(node)

        # move to front
        self.moveToFront(node)

        return node.data

    def put(self, key: int, value: int) -> None:
        if key in self.nodeMap:
            oldNode = self.nodeMap[key]
            self.remove(oldNode)

        self.nodeMap[key] = Node(key, value)
        self.moveToFront(self.nodeMap[key])

        if len(self.nodeMap) > self.capacity:
            # evict least recently used
            lru = self.head.nxt
            self.remove(lru)
            self.nodeMap.pop(lru.key, None)