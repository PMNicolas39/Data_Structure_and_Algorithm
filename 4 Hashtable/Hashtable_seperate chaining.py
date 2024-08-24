class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table will contain array that hold linked lists: insert, retrieve & delete data
class HashTable():
    def __init__(self, capacity):
        # Kích thước tối đa của hashtable, tu71c là số lượng bucket mà bảng chứa
        self.capacity = capacity
        # variable to track the number of key-value pair that stored in hash table.
        self.size = 0
        # this is the main list of hash table. Mỗi phần tử trong table là 1 bucket và các bucket này đều None
        self.table = [None] * capacity  # None linkedlist

    # This method takes a key and return an index in the array where the key-value pair should be stored
    def _hash(self, key):
        return hash(key) % self.capacity

    # Insert method will insert a key-value pair into the hash table.
    def insert(self, key, value):
        # take the index by using _hash method
        index = self._hash(key)

        if self.table[index] is None:
            self.table[index] = Node(key, value)
            # increase the size count when a new key-value pair
            # is inserted into the hash table
            self.size += 1
        else:
            # iterate through the list till the last node is found or the key already exists
            current = self.table[index]
            while current:
                if current.key == key:
                    current.value = value
                    return
                # If it doesn't find the key, it creates a new node and
                # adds it to the head of the list
                current = current.next
            new_node = Node(key, value)
            new_node.next = self.table[index]
            self.table[index] = new_node
            self.size += 1

    # get a value for a key
    def search(self, key):
        # Get the index by using _hash method
        index = self._hash(key)
        # Put index into hashmap
        current = self.table[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        raise KeyError(key)

    def remove(self, key):
        index = self._hash(key)

        previous = None
        current = self.table[index]
        while current:
            if current.key == key:
                # Sau khi dùng lệnh while current để traverse (duyet) qua từng node trong linkedlist
                # thì previous đã thành current, và current thành current.next. Previous = None tại vòng lặp đầu tiên
                if previous:
                    previous.next = current.next
                else:
                    # previous is None -> cần cập nht bucket tại vị trí index để trỏ tới node tiếp theo
                    # current.next, thay vì trỏ tới node hiện tại
                    self.table[index] = current.next
                # báo hiệu giảm 1 số trong bucket
                self.size -= 1
                return
            previous = current
            current = current.next
        raise KeyError(key)

    # Print string of hash table
    def __str__(self):
        # Empty list
        elements = []
        for i in range(self.capacity):
            current = self.table[i]
            while current is not None:
                elements.append((current.key, current.value))
                current = current.next
        return str(elements)


    # Check function of python if a key exist in hash table or not
    def __contains__(self, key):
        try:
            self.search(key)
            return True
        # KeyError dc dùng để catch key không tồn tại, và trả về giá trị False
        except KeyError:
            return False

    # Len of hash table
    def __len__(self):
        return self.size


# Drive code
if __name__ == '__main__':
    # Create a hash table with a capacity of (5)
    ht = HashTable(5)

    # Add some key-value pairs to the hash table
    ht.insert("apple", 3)
    ht.insert("banana", 2)
    ht.insert("cherry", 5)
    # Check if the hash table contains a key
    print("apple" in ht) #True
    print("durian" in ht) #False

    # get the value for a key
    print(ht.search("banana"))

    # Update a value for a key
    ht.insert("banana", 4)
    print(ht.search("banana"))

    ht.remove("apple")
    # check the size of hash table
    print(len(ht))
