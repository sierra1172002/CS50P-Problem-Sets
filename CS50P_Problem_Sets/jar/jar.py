class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("Capacity cannot be negative.")
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return self.size*"🍪"

    def deposit(self, n):
        if self.size + n > self.capacity:
            raise ValueError(f"The Jar's capacity is {self.capacity}.")
        self._size += n

    def withdraw(self, n):
        if self.size < n:
            raise ValueError(f"There are only {self.size} cookies in the jar.")
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size
