class Linear_Probing_Hash_Table:
    # Create key & value used in bucket
    def __init__(self, size):
        self.size = size
        self.keys = [None] * size  # List
        self.values = [None] * size  # List

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        while self.keys[index] is not None:
            if self.keys[index] == key:
                self.values[index] = value
                return
            index = (index + 1) % self.size
        self.keys[index] = key
        self.values[index] = value

    # Get value from key
    def get(self, key):
        index = self.hash_function(key)
        # Linear probing to find the key:
        while self.keys[index] is not None:
            if self.keys[index] == key:
                return self.values[index]
            index = (index + 1) % self.size
        # Key not found
        return None


hash_table = Linear_Probing_Hash_Table(10)
hash_table.insert('apple', 7)
hash_table.insert('banana', 10)
print(hash_table.get('apple'))
print(hash_table.get('grape'))
