class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return self.size * "🍪"


    def deposit(self, n):
        if self.size + n > self.capacity:
            raise ValueError("Deposit results in exceeded capacity")
        self.size += n

    def withdraw(self, n):
        if self.size - n < 0:
            raise ValueError("Not enough cookies available")
        self.size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

    @capacity.setter
    def capacity(self, capacity):
        if capacity < 0:
            raise ValueError("Enter a non-negative number")
        self._capacity = capacity

    @size.setter
    def size(self, size):
        if size > self.capacity:
            raise ValueError("Results in exceedd capacity")
        self._size = size


def main():
    print(str(Jar()))


if __name__ == "__main__":
    main()
