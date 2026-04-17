class MyHashSet:

    def __init__(self):
        self.data = [False, False]

    def add(self, key: int) -> None:
        while key >= len(self.data):
            self.data.extend([False] * len(self.data))
        self.data[key] = True

    def remove(self, key: int) -> None:
        if key < len(self.data):
            self.data[key] = False

    def contains(self, key: int) -> bool:
        if key >= len(self.data):
            return False
        return self.data[key]

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)