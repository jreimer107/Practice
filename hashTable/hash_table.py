
class HashTable:
    def __init__(self, capacity = 8) -> None:
        self.array = [None] * capacity
        self.size = 0
        self.capacity = capacity


    def _get_index(self, key):
        index = hash(key) % self.capacity

        while self.array[index] and self.array[index][0] != key:
            index += 1

        return index

    def _expand(self):
        self.capacity *= 2
        old_array = self.array
        self.array = [None] * self.capacity
        for pair in old_array:
            if pair:
                self.add(pair[0], pair[1])

    def add(self, key, value):
        if self.size == self.capacity:
            self._expand()

        index = self._get_index(key)

        self.array[index] = [key, value]
        self.size += 1

    def get(self, key):
        index = self._get_index(key)

        return self.array[index][1]

    def remove(self, key):
        index = self._get_index(key)
        self.array[index] = None
        self.size -= 1